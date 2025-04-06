from pydantic import BaseModel

class CropRequest(BaseModel):
    farmer_id: str
    crop_name: str
    quantity: float
    willing_to_sell: bool

class CropResponse(BaseModel):
    success: bool
    message: str
