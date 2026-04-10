from src.services.repository import UserRepository
from src.services.logger import log_structured
import os

repo = UserRepository(os.environ["USERS_TABLE"])

def handler(event, context):
    user_id = event.get("pathParameters", {}).get("id") # Si viene de API Gateway
    try:
        log_structured("INFO", "Iniciando obtención de usuario", {"user_id": user_id})
        user = repo.get(user_id)
        return {"statusCode": 20, "status": "SUCCESS","body": user}
    except Exception as e:
        log_structured("ERROR", "Fallo en obtención de usuario", {"error": str(e), "user_id": user_id})
        raise e # Re-lanzamos para que Step Functions capture el error