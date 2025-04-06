from fastapi import APIRouter, HTTPException
from app.models.weather_model import WeatherRequest, WeatherResponse
from app.services.weather_service import get_weather_and_planting_times

router = APIRouter()

@router.post("/")
async def weather_info(weather_request: WeatherRequest):
    try:
        info = get_weather_and_planting_times(weather_request)
        return WeatherResponse(success=True, info=info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
