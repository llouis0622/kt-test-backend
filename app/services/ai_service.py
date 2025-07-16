import os
from dotenv import load_dotenv

load_dotenv()
AI_API_KEY = os.getenv("AI_API_KEY")

def get_ai_answer(question: str) -> str:
    # 실제로는 AI_API_KEY를 활용해 외부 API 호출
    return f"'{question}'에 대한 답변입니다. (AI 연동 필요)" 