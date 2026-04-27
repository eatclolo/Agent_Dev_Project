from pydantic import BaseModel
from typing import Optional


class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    query: str 
    answer: str
    error: Optional[str]
