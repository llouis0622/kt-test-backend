from pydantic import BaseModel

class SelectRequest(BaseModel):
    option_id: int 