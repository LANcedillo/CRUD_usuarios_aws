import pytest
from src.services.repository import UserRepository
from src.models.user import UserResponse
from src.handlers.validator import handler

def test_handler_valid_data():
    event = {
        "username": "senior_dev",
        "email": "test@example.com",
        "edad": 25
    }
    
    response = handler(event, None)
    assert response["statusCode"] == 200
    assert response["body"]["username"] == "senior_dev"

def test_handler_invalid_age():
    event = {
        "username": "junior",
        "email": "error@test.com",
        "edad": 15
    }
    
    with pytest.raises(Exception) as excinfo:
        handler(event, None)
    
    assert "Error de validación" in str(excinfo.value)


def test_save_user_in_dynamo_mock(dynamodb_mock):
    repo = UserRepository("UsersTable")
    user_test = {"username": "test_user", "email": "test@test.com", "edad": 30}
    user = UserResponse(**user_test)
    repo.save_user(user)
    response = repo.get(str(user.user_id))
    assert response["username"] == user_test["username"]
    assert response["email"] == user_test["email"]
    assert response["edad"] == user_test["edad"]
    