from src.models.user import UserCreate
from src.services.logger import log_event
import json

def handler(event, context):
    log_event("Recibiendo evento de registro", {"event": event})
    
    try:
        user = UserCreate(**event)
        log_event("Validación exitosa", {"user_id": str(user.username)})
        return {
            "statusCode": 200,
            "body": user.model_dump()
        }
    except Exception as e:
        log_event("Error de validación", {"error": str(e)})
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Datos inválidos", "details": str(e)})
        }