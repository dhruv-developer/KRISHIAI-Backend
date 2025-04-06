from fastapi import APIRouter, HTTPException
from app.models.feedback_model import FeedbackRequest, FeedbackResponse
from app.services.feedback_service import submit_feedback

router = APIRouter()

@router.post("/", response_model=FeedbackResponse)
async def send_feedback(feedback_request: FeedbackRequest):
    try:
        message = submit_feedback(feedback_request)
        return FeedbackResponse(success=True, message=message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
