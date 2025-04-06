from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    farmer_id: str
    feedback: str

class FeedbackResponse(BaseModel):
    success: bool
    message: str
