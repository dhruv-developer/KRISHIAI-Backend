from fastapi import APIRouter, HTTPException
from app.models.help_model import HelpRequest, HelpResponse
from app.services.help_service import get_help_center_info

router = APIRouter()

@router.post("/")
async def help_center(help_request: HelpRequest):
    try:
        info = get_help_center_info(help_request)
        return HelpResponse(success=True, info=info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
