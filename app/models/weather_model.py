from pydantic import BaseModel

class WeatherRequest(BaseModel):
    location: str

class WeatherResponse(BaseModel):
    success: bool
    info: dict  # Contains weather data and time advice
