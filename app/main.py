from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat, category, select

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포시에는 프론트엔드 주소로 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category.router)
app.include_router(chat.router)
app.include_router(select.router) 