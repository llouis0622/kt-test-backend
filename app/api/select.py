from fastapi import APIRouter
from app.models.select import SelectRequest

router = APIRouter()

@router.post("/select")
def select(req: SelectRequest):
    return {"info": f"선택하신 옵션({req.option_id})에 대한 정보입니다."} 