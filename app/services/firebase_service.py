import firebase_admin
from firebase_admin import credentials, messaging
from app.config import settings

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(settings.firebase_credential_path)
    firebase_admin.initialize_app(cred)

def send_sms_notification(sms_request):
    # Here we treat the phone_number as a device token for demonstration.
    message = messaging.Message(
        data={
            "message": sms_request.message,
            "language": sms_request.language,
        },
        token=sms_request.phone_number,  # In real apps, use proper device tokens.
    )
    response = messaging.send(message)
    return f"Message sent with response: {response}"
