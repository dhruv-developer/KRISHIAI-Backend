import razorpay
from app.config import settings

client = razorpay.Client(auth=(settings.razorpay_key_id, settings.razorpay_key_secret))

def create_order(payment_request):
    order_data = {
        "amount": payment_request.amount,
        "currency": payment_request.currency,
        "receipt": payment_request.receipt,
        "notes": payment_request.notes,
        "payment_capture": 1
    }
    order = client.order.create(data=order_data)
    return order

def verify_payment(verification_request):
    params_dict = {
        "razorpay_order_id": verification_request.razorpay_order_id,
        "razorpay_payment_id": verification_request.razorpay_payment_id,
        "razorpay_signature": verification_request.razorpay_signature,
    }
    try:
        client.utility.verify_payment_signature(params_dict)
        return True
    except razorpay.errors.SignatureVerificationError:
        return False
