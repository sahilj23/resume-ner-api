from pydantic import BaseModel
from typing import Dict, List

class ResumeRequest(BaseModel):
    text: str

class ResumeResponse(BaseModel):
    entities: Dict[str, List[str]]
