from fastapi import APIRouter, HTTPException
from app.models.payment_model import PaymentCreateRequest, PaymentCreateResponse, PaymentVerificationRequest, PaymentVerificationResponse
from app.services.razorpay_service import create_order, verify_payment

router = APIRouter()

@router.post("/create", response_model=PaymentCreateResponse)
async def create_payment_order(payment_request: PaymentCreateRequest):
    try:
        order = create_order(payment_request)
        return PaymentCreateResponse(success=True, order_id=order["id"], message="Order created successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify", response_model=PaymentVerificationResponse)
async def verify_payment_signature(verification_request: PaymentVerificationRequest):
    try:
        is_valid = verify_payment(verification_request)
        if is_valid:
            return PaymentVerificationResponse(success=True, message="Payment verified successfully")
        else:
            return PaymentVerificationResponse(success=False, message="Payment verification failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
