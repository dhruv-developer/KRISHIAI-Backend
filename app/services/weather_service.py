import requests
from app.config import settings

def get_weather_and_planting_times(weather_request):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": weather_request.location,
        "appid": settings.openweather_api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()

    temp = data["main"]["temp"]
    # Determine planting advice based on temperature
    if 20 < temp < 30:
        planting_time = "Ideal for planting"
    else:
        planting_time = "Not ideal for planting"

    # Use weather condition to advise on selling times
    if data["weather"][0]["main"].lower() in ["clear", "clouds"]:
        selling_time = "Good time for selling"
    else:
        selling_time = "Not a good time for selling"

    return {
        "weather": data,
        "planting_time_advice": planting_time,
        "selling_time_advice": selling_time,
    }
