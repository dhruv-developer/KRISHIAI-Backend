import requests
from app.config import settings

def get_prices(price_request):
    params = {"product_type": price_request.product_type}
    if price_request.crop_name:
        params["crop_name"] = price_request.crop_name

    response = requests.get(settings.product_api_url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data

def register_crop_sale(crop_request):
    from firebase_admin import firestore
    db = firestore.client()
    # Save the sale registration in the "crop_sales" collection.
    doc_ref = db.collection("crop_sales").document(crop_request.farmer_id)
    doc_ref.set(crop_request.dict())
    return "Crop sale registered successfully."

def check_crop_prices(crop_name):
    from app.models.price_model import PriceRequest
    price_request = PriceRequest(product_type="crop", crop_name=crop_name)
    return get_prices(price_request)
