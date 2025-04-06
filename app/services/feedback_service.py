def submit_feedback(feedback_request):
    from firebase_admin import firestore
    db = firestore.client()
    # Store feedback in the "feedback" collection
    doc_ref = db.collection("feedback").document(feedback_request.farmer_id)
    doc_ref.set(feedback_request.dict())
    return "Feedback submitted successfully."
