from pydantic import BaseModel

class HelpRequest(BaseModel):
    query: str

class HelpResponse(BaseModel):
    success: bool
    info: str
