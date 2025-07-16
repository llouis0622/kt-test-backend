from pydantic import BaseModel
from typing import Optional, Dict

class ChatRequest(BaseModel):
    question: str
    context: Optional[Dict] = None 