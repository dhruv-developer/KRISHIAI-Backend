from fastapi import APIRouter, HTTPException
from app.models.ai_agent_model import AIRequest, AIResponse
from app.services.groq_service import get_ai_response

router = APIRouter()

@router.post("/agent", response_model=AIResponse)
async def ai_agent(ai_request: AIRequest):
    try:
        response_text = get_ai_response(ai_request)
        return AIResponse(success=True, response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
