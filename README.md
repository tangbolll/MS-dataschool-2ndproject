# MS-dataschool-2ndproject

<img width="1118" height="629" alt="Image" src="https://github.com/user-attachments/assets/05577c2e-852b-4141-8174-d4b3c05e99f1" />

### 📸 프로젝트 시연 화면

| **현황 대시보드** | **소비금액 대시보드** |
|:--------------------------:|:----------------------------:|
| <img src="https://github.com/user-attachments/assets/5249a817-70b3-46fb-ae13-7fd33bcbf5a8" width="400"/> | <img src="https://github.com/user-attachments/assets/8d1a7adf-ad05-432f-bacf-ebdd0779d29a" width="400"/> |

| **유동인구 대시보드** | **체류시간 대시보드** |
|:--------------------------:|:----------------------:|
| <img src="https://github.com/user-attachments/assets/16873736-486c-4efe-9ce9-178cdecc1142" width="400"/> | <img src="https://github.com/user-attachments/assets/cefc1edc-e2f6-4dd1-b130-0217ea96c3c4" width="400"/> |

| **혼잡도 대시보드** | |
|:------------------------------:|:--:|
| <img src="https://github.com/user-attachments/assets/fc7a747d-4001-45d8-baf6-b55348d5783d" width="400"/> | |


## 🔧 사용 기술 스택

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) </br>
![Azure VM](https://img.shields.io/badge/Azure%20VM-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure Function](https://img.shields.io/badge/Azure%20Function-0062AD?style=for-the-badge&logo=azurefunctions&logoColor=white)
![Event Hub](https://img.shields.io/badge/Event%20Hub-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![Cosmos DB](https://img.shields.io/badge/Cosmos%20DB-0078D4?style=for-the-badge&logo=azurecosmosdb&logoColor=white)
![Blob Storage](https://img.shields.io/badge/Blob%20Storage-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) </br>
![Azure ML](https://img.shields.io/badge/Azure%20ML-0078D4?style=for-the-badge&logo=azureml&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-EA3621?style=for-the-badge&logo=databricks&logoColor=white)
![Data Factory](https://img.shields.io/badge/Data%20Factory-0062AD?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure AI Search](https://img.shields.io/badge/Azure%20AI%20Search-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white) </br>
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-0078D4?style=for-the-badge&logo=openai&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)


### 🎯 대시보드 목적 및 배경

- **개발 배경**:
    
    서울시 지역 기반 유동인구와 업종별 소비 데이터를 실시간으로 추적하고, 상권별 소비 트렌드를 분석하여 소상공인의 마케팅 전략 수립을 지원하기 위함
    
- **대시보드의 핵심 목적**:
    - 캠페인 효과 분석
        - 캠페인 진행 구간 내 소비자 유입 변화 추이 (예: 캠페인 시작 후 유동인구 대비 카드 소비건수 증가율)
        - 캠페인 전·후 업종별 카드 결제 건수 및 총 결제 금액 변화
        - 광고 실행 이후 신규 고객 비율 변화 (추정치 기반)
    - 고객 유입 채널별 전환률 추적
        - 시간대별 유동인구 수 대비 업종별 카드 결제율
        - 주요 교통수단별 유입비율 (예: 버스/지하철 하차량)과 해당 시간대 소비율
        - 연령대별 유입수 대비 소비 전환율
    - KPI 실적 현황 공유
        - 일/주/월 단위 상권 방문자 수, 총 소비 금액, 객단가 변화 추이
        - 목표 대비 실제 소비 유입률 (목표 소비 금액 설정 가능)

---

### 👤ⅱ 타겟 사용자

| 구분 | 사용자 | 주요 니즈 | 활용 방식 |
| --- | --- | --- | --- |
| 자영업자 | 운영자 (1-2인) | 유입 시간대, 고객 체류, 관심 업종,매장 운영 전략, 마케팅 타이밍 조정  | 일일 점검, 이벤트 후 확인 |
| 중소기업 마케팅팀 | 프로모션 기획자 | 타겟 도달률, 유입-소비율, 채널별 전환퍼널 분석, 타이밍 조정 ,콘텐츠 전략 설계 | 사전/사후 비교 |
| 공공기관 | 지역행사 담당자 | 상권 활성화, 혼잡도, 행사 일정 계획,지원 타겟 선정 | 정기 모니터링, 성과 분석 |
| 로컬 콘텐츠 기획자 | 청년 창업가 | 체류 특성, 시간대 활용, 타겟층 도출,점포 입지 비교,사업계획  참고 | 주간 흐름 분석 |

### ✅ 1. **지역 상권 자영업자 (1인 경영자)**

- **구분**: 자영업자
- **사용자**: 1인 경영자 (카페, 음식점, 소매업 등)
- **주요 니즈**:
    - 내 점포 주변 유동인구 흐름과 **고객 체류 시간대 파악**
    - **시간대별 소비 패턴** 변화 감지 (예: 점심 시간 vs 저녁 시간)
    - 내 업종에 대한 지역 주민의 **관심도 및 방문율** 추이
- **활동 양식**:
    - **일일 점검** (오픈 전 or 마감 후 유동인구 흐름 확인)
    - 신규 메뉴 출시 or 이벤트 전후의 **캠페인 효과 추적**
- **활용 기대**:
    - 영업시간/메뉴 구성/광고 타이밍 최적화

---

### ✅ 2. **중소기업 마케팅팀 프로모션 기획자**

- **구분**: 중소기업 마케팅팀
- **사용자**: 온·오프라인 프로모션 기획자
- **주요 니즈**:
    - 특정 지역에서 **우리 브랜드가 타겟층에게 도달하고 있는지 여부 확인**
    - 캠페인 이전·이후의 **유입 인구 및 카드 소비 증가율**
    - **주요 이동 루트 및 혼잡 시간대** 파악을 통한 행사 시간 결정
- **활동 양식**:
    - **프로모션 사전·사후 비교 분석**
    - **월 단위 성과 리포트용 지표 추출**
- **활용 기대**:
    - 타겟 지역 선정 정확도 향상, 광고 효율성 향상

---

### ✅ 3. **공공기관 지역활성화 담당자**

- **구분**: 공공기관
- **사용자**: 지역축제, 거리 행사, 전통시장 기획 담당자
- **주요 니즈**:
    - 지역 내 상권 활성화 지표(소비, 유입, 혼잡도) 기반으로 **행사 개최 시기/장소 결정**
    - 타 행사와의 일정 겹침 여부 확인
    - 정책 효과성 평가를 위한 **전후 소비 데이터 추적**
- **활동 양식**:
    - **정기적 모니터링** (주간, 월간 지역 데이터 추이 분석)
    - **정책/행사 사전 사후 성과 비교**
- **활용 기대**:
    - 행사 기획의 타당성 확보, 정책 성과 데이터 확보

---

### ✅ 4. **로컬 크리에이터 / 소셜벤처 기획자**

- **구분**: 공공/민간 복합
- **사용자**: 지역 콘텐츠 기획자, 청년 창업가, 공간 운영자
- **주요 니즈**:
    - 특정 지역에서 **시민의 이동 흐름과 체류 특성 분석**
    - **시간대별 상권 분위기 파악**(낮/밤/주말/공휴일)
    - 상권 내 소비력이 높은 고객군 분석 (청년, 가족 등)
- **활동 양식**:
    - **이벤트 전 후 비교, 활동공간 기획 참고용**
    - 주간 단위 흐름 모니터링
- **활용 기대**:
    - 지역 기반 콘텐츠 타겟 설정, 프로젝트 타당성 검증
  

### 1. 유동인구수 Logic Tree 매핑

| 로직 트리 항목 | 데이터 컬럼 (또는 파생 컬럼) | 설명 |
| --- | --- | --- |
| **유출 경로별 인구수** |  |  |
| └ 버스 유출 | `BUS_ACML_GTOFF_PPLTN_MAX`, `BUS_5WTHN_GTOFF_PPLTN_MAX` | 버스 하차 인원 |
| └ 지하철 유출 | `SUB_ACML_GTOFF_PPLTN_MAX`, `SUB_5WTHN_GTOFF_PPLTN_MAX` | 지하철 하차 인원 |
| └ 기타 유출 | **파생 필요** (`따릉이, 도보 추정`) | 거치율, 날씨 등으로 추정 가능 |
| **유입 경로별 인구수** |  |  |
| └ 버스 유입 | `BUS_ACML_GTON_PPLTN_MAX`, `BUS_5WTHN_GTON_PPLTN_MAX` | 버스 승차 인원 |
| └ 지하철 유입 | `SUB_ACML_GTON_PPLTN_MAX`, `SUB_5WTHN_GTON_PPLTN_MAX` | 지하철 승차 인원 |
| └ 기타 유입 | **파생 필요** (`행사/따릉이/도보 등`) | 문화행사명, 따릉이 |
| **유입 시간별 인구수** | `PPLTN_TIME`, `LIVE_PPLTN_STTS` | 시간별 실시간 인구수 |
| └ 요일별 순유입 | `PPLTN_TIME` + 파생 요일 컬럼 | 날짜 기준 요일 추출 |
| └ 시간별 순유입 | `PPLTN_TIME` 기반 시간대 집계 | 시계열 분석 가능 |

---

### 2. 소비금액 Logic Tree 매핑

| 로직 트리 항목 | 데이터 컬럼 | 설명 |
| --- | --- | --- |
| **소비 업종** | `RSB_LRG_CTGR`, `RSB_MID_CTGR` | 업종 대/중분류 |
| └ 업종별 소비건수 | `RSB_SH_PAYMENT_CNT` | 업종 기준 결제 건수 |
| └ 업종별 소비금액 | `RSB_SH_PAYMENT_AMT_MIN`, `MAX` | 업종 기준 소비 금액 |
| **소비자 유형** |  |  |
| └ 기존/신규 유저 소비건수 | **파생 필요** | 누적 또는 CRM 연계 필요 |
| └ 연령별 소비건수 | `CMRCL_10_RATE`~`CMRCL_60_RATE` (비율) | 연령별 소비 비율 |
| └ 성별 소비건수 | `CMRCL_MALE_RATE`, `CMRCL_FEMALE_RATE` | 성별 소비 비율 |
| **시간대별 소비금액** | `AREA_SH_PAYMENT_AMT_MIN`, `MAX` + `CMRCL_TIME` | 시간 기준 집계 |
| └ 객단가 변화량 | `결제금액 / 결제건수` → 파생 | 객단가 파생 컬럼 |
| **소비 위치** | `AREA_NM`, `ADDRESS`, `LAT`, `LNG` | 장소/위치 정보 |

---

### 3. 체류시간 Logic Tree 매핑

| 로직 트리 항목 | 데이터 컬럼 또는 파생 | 설명 |
| --- | --- | --- |
| **평균 체류 특성** |  |  |
| └ 인구 수 | `LIVE_PPLTN_STTS`, `AREA_PPLTN_MIN/MAX` | 실시간 인구 |
| └ 인구 수 범위 | `AREA_PPLTN_MIN`, `AREA_PPLTN_MAX` | 인구 변동 범위 |
| └ 혼잡도 단계 | `AREA_CONGEST_LVL`, `AREA_CONGEST_MSG` | 혼잡도 수준 |
| └ 체류 시간 (분석값) | **파생 필요** → `유입 ~ 유출` 시간 간 차이 | 순수 체류시간 파생 |
| └ 시간대/요일별 평균 | `PPLTN_TIME` 기반 집계 | 평균 계산 |
| **체류자 속성** |  |  |
| └ 성별 비율 | `MALE_PPLTN_RATE`, `FEMALE_PPLTN_RATE` | 실시간 성비 |
| └ 연령대 별 비율 | `PPLTN_RATE_10`~`70` | 실시간 연령대 |
| └ 상주/비상주 인구 비율 | `RESNT_PPLTN_RATE`, `NON_RESNT_PPLTN_RATE` | 체류자 유형 분류 |
| └ 상주 방문 주기 | **파생 필요 (외부 데이터 필요)** | 상주자 주기적 방문 여부 |
| └ 비상주 체류시간 평균 | **파생 필요: 상주/비상주 분리 후 체류시간 집계** |  |
