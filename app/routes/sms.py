from fastapi import APIRouter, HTTPException
from app.models.sms_model import SMSRequest, SMSResponse
from app.services.firebase_service import send_sms_notification

router = APIRouter()

@router.post("/send", response_model=SMSResponse)
async def send_sms(sms_request: SMSRequest):
    try:
        result = send_sms_notification(sms_request)
        return SMSResponse(success=True, detail=result)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
