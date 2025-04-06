from fastapi import FastAPI
from app.routes import sms, prices, help, weather, crops, ai_agent, payment, feedback

app = FastAPI(title="AgriTech Backend API")

app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(crops.router, prefix="/crops", tags=["Crops"])
app.include_router(ai_agent.router, prefix="/ai", tags=["AI Agent"])
app.include_router(payment.router, prefix="/payment", tags=["Payment"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(sms.router, prefix="/sms", tags=["SMS"])
# app.include_router(prices.router, prefix="/prices", tags=["Prices"])
# app.include_router(help.router, prefix="/help", tags=["Help"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AgriTech API"}
