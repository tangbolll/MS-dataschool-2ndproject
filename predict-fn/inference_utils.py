import pandas as pd
import numpy as np
from datetime import timedelta
import logging
import gc

def preprocess_data(df):
    """데이터 전처리"""
    try:
        logging.info("🔧 데이터 전처리 시작...")
        
        # 시간 컬럼 변환
        if 'inserted_at' in df.columns:
            df['inserted_at'] = pd.to_datetime(df['inserted_at'])
        
        # 정렬
        df = df.sort_values(by="inserted_at")
        
        # 결측치 처리
        df = df.dropna()
        
        logging.info(f"✅ 전처리 완료: {df.shape}")
        return df
        
    except Exception as e:
        logging.error(f"❌ 전처리 중 오류: {str(e)}")
        raise

def predict_next_row(df, models, scalers, target_columns, feature_columns, lookback_window=12):
    """다음 30분 후 예측 - 메모리 효율성 개선"""
    try:
        logging.info("🔮 예측 함수 시작...")
        
        # 최근 데이터 가져오기
        recent_data = df.tail(lookback_window)
        
        # 피처 행 구성
        feature_row = []
        
        for col in feature_columns:
            if col in recent_data.columns:
                val = recent_data[col].values[-1]
                # NaN 체크
                if pd.isna(val):
                    val = 0
            else:
                val = 0
            feature_row.append(val)
        
        # 시간 특성 추가
        last_time = df.iloc[-1]['inserted_at']
        next_time = pd.to_datetime(last_time) + timedelta(minutes=30)
        
        # 시간 특성 추가
        feature_row.extend([next_time.hour, next_time.weekday(), next_time.month])
        
        logging.info(f"📊 피처 행 크기: {len(feature_row)}")
        
        # NumPy 배열로 변환
        feature_array = np.array(feature_row).reshape(1, -1)
        
        # 스케일링
        feature_scaled = scalers['feature_scaler'].transform(feature_array)
        
        logging.info("🔄 모델 예측 시작...")
        
        # 예측 (메모리 효율적으로)
        predictions = {}
        
        for i, col in enumerate(target_columns):
            try:
                model = models[col]
                target_scaler = scalers[f"{col}_scaler"]
                
                # 예측 수행
                pred_scaled = model.predict(feature_scaled)
                
                # 스케일 역변환
                pred_original = target_scaler.inverse_transform(pred_scaled.reshape(-1, 1)).flatten()[0]
                
                predictions[col] = pred_original
                
                # 메모리 정리
                del pred_scaled
                
                if (i + 1) % 10 == 0:  # 10개마다 로그
                    logging.info(f"📈 예측 진행: {i+1}/{len(target_columns)}")
                    gc.collect()
                
            except Exception as e:
                logging.error(f"❌ {col} 예측 중 오류: {str(e)}")
                predictions[col] = 0  # 기본값 설정
        
        # 결과 DataFrame 생성
        pred_row = predictions.copy()
        pred_row["inserted_at"] = next_time
        pred_row["hour"] = next_time.hour
        pred_row["day_of_week"] = next_time.weekday()
        pred_row["month"] = next_time.month
        
        result_df = pd.DataFrame([pred_row])
        
        # 메모리 정리
        del feature_array, feature_scaled, predictions, pred_row
        gc.collect()
        
        logging.info("✅ 예측 완료")
        
        return result_df
        
    except Exception as e:
        logging.error(f"❌ 예측 중 오류: {str(e)}")
        import traceback
        logging.error(f"📋 상세 오류: {traceback.format_exc()}")
        raise