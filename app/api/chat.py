from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.ai_service import get_ai_answer

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    answer = get_ai_answer(req.question)
    return {"answer": answer} 