from app.services.huggingface_service import query_model
from app.models.help_model import HelpRequest

def get_help_center_info(help_request: HelpRequest) -> str:
    return query_model(help_request.query)
