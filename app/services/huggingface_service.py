import requests
from app.config import settings

def query_model(query, model_name="deepset/roberta-base-squad2"):
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {settings.huggingface_api_key}"} if settings.huggingface_api_key else {}
    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
    data = response.json()
    # Process the response – adjust as per model output
    if isinstance(data, list) and len(data) > 0 and "answer" in data[0]:
        return data[0]["answer"]
    else:
        return str(data)
