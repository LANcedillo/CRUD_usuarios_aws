from src.services.repository import UserRepository
from src.services.logger import log_structured
import os

# Instanciamos el repositorio FUERA del handler para reutilizar la conexión (Best Practice)
repo = UserRepository(os.environ["USERS_TABLE"])

def handler(event, context):
    user_data = event.get("body")
    try:
        log_structured("INFO", "Iniciando persistencia en DynamoDB", {"user_id": user_data.get("user_id")})
        repo.create(user_data)
        return {"statusCode": 201, "status": "SUCCESS"}
    except Exception as e:
        log_structured("ERROR", "Fallo en persistencia", {"error": str(e), "user_id": user_data.get("user_id")})
        raise e # Re-lanzamos para que Step Functions capture el error