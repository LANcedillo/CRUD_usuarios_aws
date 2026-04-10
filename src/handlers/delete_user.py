from services.repository import UserRepository
from src.services.logger import log_structured
import os

# Instanciamos el repositorio FUERA del handler para reutilizar la conexión
repo = UserRepository(os.environ["USERS_TABLE"])

def handler(event, context):
    user_id = event["pathParameters"]["id"]
    try:
        log_structured("INFO", "Iniciando eliminación de usuario", {"user_id": user_id})
        repo.delete(user_id)
        return {"statusCode": 204, "status": "SUCCESS"}
    except Exception as e:
        log_structured("ERROR", "Fallo el borrado del usuario", {"error": str(e), "user_id": user_id})
        raise e # Re-lanzamos para que Step Functions capture el error