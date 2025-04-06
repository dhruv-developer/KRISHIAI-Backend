from pydantic import BaseModel

class PaymentCreateRequest(BaseModel):
    amount: int  # Amount in smallest currency unit (e.g., paise for INR)
    currency: str
    receipt: str
    notes: dict = {}

class PaymentCreateResponse(BaseModel):
    success: bool
    order_id: str
    message: str

class PaymentVerificationRequest(BaseModel):
    razorpay_payment_id: str
    razorpay_order_id: str
    razorpay_signature: str

class PaymentVerificationResponse(BaseModel):
    success: bool
    message: str
