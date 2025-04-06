from pydantic import BaseModel
from typing import Dict

class PriceRequest(BaseModel):
    product_type: str  # e.g., "fertilizer", "seed", "crop"
    crop_name: str = None  # Only for crop prices

class PriceResponse(BaseModel):
    success: bool
    prices: Dict[str, float]  # mapping product names to their prices
