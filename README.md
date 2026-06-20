# 팀 업무 대시보드

Streamlit을 이용한 팀 업무 관리 대시보드입니다.

## 기능

- 📅 **최근 일정**: 팀의 예정된 일정 표시
- 📋 **카테고리별 업무 현황**: MDR, FDA, CyberSecurity, GMP, MFDS 분류별 프로젝트 관리
- 🔍 **카테고리 필터**: 사이드바에서 관심있는 카테고리만 선택하여 조회
- 🎨 **상태별 색상**: 업무 상태에 따른 시각적 구분

## 프로젝트 상태

- ✅ 완료: 초록색
- ⏳ 대기중: 노란색
- 🔄 진행중: 기본색
- 👀 검토중: 기본색

## 설치 방법

```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
streamlit run app.py
```

앱이 브라우저에서 `http://localhost:8501`로 열립니다.

## 파일 구조

```
.
├── app.py                 # Streamlit 메인 애플리케이션
├── tasks.json             # 업무 데이터 (JSON 형식)
├── requirements.txt       # Python 패키지 의존성
├── .streamlit/
│   └── config.toml        # Streamlit 설정
└── README.md
```

## 데이터 형식 (tasks.json)

각 카테고리별로 프로젝트 정보를 저장합니다:

```json
{
  "카테고리": [
    {
      "project": "프로젝트명",
      "status": "상태 (완료/대기중/진행중/검토중)",
      "update": "최근 업데이트 날짜",
      "note": "비고 내용"
    }
  ],
  "Schedule": [
    {
      "date": "YYYY-MM-DD",
      "client": "고객사명",
      "manager": "담당자명"
    }
  ]
}
```
