# 부산시 청년 창업 챗봇 백엔드 (FastAPI)

## 소개
부산시 청년 창업 관련 정보를 제공하는 챗봇 백엔드입니다. FastAPI 기반으로 개발되었습니다.

## 실행 방법
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 배포 방법 (Docker)
```bash
docker build -t kt-backend .
docker run -d -p 8000:8000 --env-file .env kt-backend
```

## 주요 구조
- app/
  - main.py: FastAPI 진입점
  - api/: API 라우터
  - models/: Pydantic 모델
  - services/: 비즈니스 로직, AI 연동
  - data/: 임시 데이터 