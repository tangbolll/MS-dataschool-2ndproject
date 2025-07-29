import azure.functions as func
import logging
import os
import io
import pandas as pd
import joblib
import gc
from azure.storage.blob import BlobServiceClient
from datetime import timedelta
from inference_utils import preprocess_data, predict_next_row

app = func.FunctionApp()

# 전역 변수로 모델 캐싱
_models = None
_scalers = None
_target_columns = None
_feature_columns = None
_model_loaded = False

def load_models_once():
    """모델을 한 번만 로드하고 전역 변수에 저장"""
    global _models, _scalers, _target_columns, _feature_columns, _model_loaded
    
    if _model_loaded:
        return _models, _scalers, _target_columns, _feature_columns
    
    try:
        # 연결 문자열 가져오기
        conn_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
        blob_service = BlobServiceClient.from_connection_string(conn_str)
        container_name = "dt026test"

        # 청크 단위 로딩 함수
        def load_large_pickle(blob_path, chunk_size=8*1024*1024):  # 8MB 청크
            try:
                blob_client = blob_service.get_blob_client(container=container_name, blob=blob_path)
                if not blob_client.exists():
                    raise FileNotFoundError(f"Blob '{blob_path}' does not exist")
                
                logging.info(f"🔄 '{blob_path}' 로딩 시작...")
                
                # 전체 스트림을 메모리에 로드
                stream = io.BytesIO()
                
                # 청크 단위로 다운로드
                blob_size = blob_client.get_blob_properties().size
                logging.info(f"📏 파일 크기: {blob_size / (1024*1024):.2f} MB")
                
                downloaded = 0
                for chunk in blob_client.download_blob().chunks():
                    stream.write(chunk)
                    downloaded += len(chunk)
                    if downloaded % (50*1024*1024) == 0:  # 50MB마다 로그
                        logging.info(f"📥 다운로드 진행: {downloaded / (1024*1024):.2f} MB / {blob_size / (1024*1024):.2f} MB")
                
                stream.seek(0)
                logging.info(f"✅ '{blob_path}' 다운로드 완료")
                
                # joblib로 로드
                result = joblib.load(stream)
                logging.info(f"✅ '{blob_path}' 역직렬화 완료")
                
                # 메모리 정리
                stream.close()
                del stream
                gc.collect()
                
                return result
                
            except Exception as e:
                logging.error(f"❌ '{blob_path}' 로딩 중 오류: {str(e)}")
                raise

        # 모델 및 부속 파일 로딩
        logging.info("🔄 모델 파일들 로딩 시작...")
        
        _models = load_large_pickle("models/models.pkl")
        logging.info("✅ 모델 로딩 완료")
        
        _scalers = load_large_pickle("models/scalers.pkl")
        logging.info("✅ 스케일러 로딩 완료")
        
        _target_columns = load_large_pickle("models/target_columns.pkl")
        logging.info("✅ 타겟 컬럼 로딩 완료")
        
        _feature_columns = load_large_pickle("models/feature_columns.pkl")
        logging.info("✅ 피처 컬럼 로딩 완료")
        
        _model_loaded = True
        
        # 메모리 정리
        gc.collect()
        
        logging.info("🎉 모든 모델 파일 로딩 완료")
        return _models, _scalers, _target_columns, _feature_columns
        
    except Exception as e:
        logging.error(f"❌ 모델 로딩 중 치명적 오류: {str(e)}")
        raise

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
def predictBlobFn(myTimer: func.TimerRequest) -> None:

    if myTimer.past_due:
        logging.info('⏰ 타이머가 지연되었습니다!')

    logging.info('🚀 Azure Function 예측 시작')

    try:
        # 모델 로드 (캐싱 사용)
        models, scalers, target_columns, feature_columns = load_models_once()
        
        # 연결 문자열 가져오기
        conn_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
        blob_service = BlobServiceClient.from_connection_string(conn_str)
        container_name = "dt026test"

        # 데이터 로드
        logging.info("📊 데이터 로딩 시작...")
        blob_data = blob_service.get_blob_client(container=container_name, blob="ML_MAIN_.csv")
        if not blob_data.exists():
            logging.error("❌ ML_MAIN_.csv 파일이 존재하지 않습니다.")
            return

        # CSV 데이터 로드
        stream = io.BytesIO()
        blob_data.download_blob().readinto(stream)
        stream.seek(0)
        df = pd.read_csv(stream)
        logging.info(f"✅ 데이터 로딩 완료: {df.shape}")
        
        # 스트림 메모리 정리
        stream.close()
        del stream

        # 전처리 및 예측
        logging.info("🔧 데이터 전처리 시작...")
        df_processed = preprocess_data(df)
        
        logging.info("🔮 예측 시작...")
        prediction = predict_next_row(df_processed, models, scalers, target_columns, feature_columns)
        
        # 메모리 정리
        del df, df_processed
        gc.collect()

        # 결과 저장
        logging.info("💾 결과 저장 시작...")
        result_stream = io.StringIO()
        prediction.to_csv(result_stream, index=False)
        result_stream.seek(0)

        result_blob = blob_service.get_blob_client(container=container_name, blob="last_prediction.csv")
        result_blob.upload_blob(result_stream.getvalue(), overwrite=True)
        
        # 결과 스트림 정리
        result_stream.close()
        del result_stream, prediction
        gc.collect()

        logging.info("🎉 예측 및 결과 저장 완료")

    except Exception as e:
        logging.error(f"❌ 예측 중 오류 발생: {str(e)}")
        import traceback
        logging.error(f"📋 상세 오류: {traceback.format_exc()}")
        
        # 메모리 정리
        gc.collect()
        
        # 오류 시 모델 캐시 초기화 (다음 실행에서 재로드)
        global _model_loaded
        _model_loaded = False