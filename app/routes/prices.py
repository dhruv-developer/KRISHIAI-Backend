from fastapi import APIRouter, HTTPException
from app.models.price_model import PriceRequest, PriceResponse
from app.services.crop_service import get_prices

router = APIRouter()

@router.post("/")
async def fetch_prices(price_request: PriceRequest):
    try:
        prices = get_prices(price_request)
        return PriceResponse(success=True, prices=prices)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
