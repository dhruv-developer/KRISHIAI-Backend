from pydantic import BaseSettings

class Settings(BaseSettings):
    firebase_credential_path: str
    groq_api_key: str
    openweather_api_key: str
    product_api_url: str
    huggingface_api_key: str = None  # Optional if not needed
    razorpay_key_id: str
    razorpay_key_secret: str

    class Config:
        env_file = ".env"

settings = Settings()
