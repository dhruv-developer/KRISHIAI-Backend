from pydantic import BaseModel

class SMSRequest(BaseModel):
    phone_number: str
    message: str
    language: str = "en"

class SMSResponse(BaseModel):
    success: bool
    detail: str
