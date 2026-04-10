from src.services.repository import UserRepository
import os

repo = UserRepository(os.environ["USERS_TABLE"])

def handler(event, context):
    user_id = event.get("pathParameters", {}).get("id") # Si viene de API Gateway
    user = repo.get(user_id)
    if not user:
        return {"statusCode": 404, "body": "User not found"}
    return {"statusCode": 200, "body": user}