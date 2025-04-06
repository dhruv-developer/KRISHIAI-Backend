from fastapi import APIRouter, HTTPException
from app.models.crop_model import CropRequest, CropResponse
from app.services.crop_service import register_crop_sale, check_crop_prices

router = APIRouter()

@router.post("/sell")
async def sell_crop(crop_request: CropRequest):
    try:
        result = register_crop_sale(crop_request)
        return CropResponse(success=True, message=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/prices/{crop_name}")
async def get_crop_price(crop_name: str):
    try:
        prices = check_crop_prices(crop_name)
        return {"success": True, "prices": prices}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
