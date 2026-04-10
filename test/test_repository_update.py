from src.services.repository import UserRepository
from src.models.user import UserResponse, UserUpdate

def test_update_user_partial(dynamodb_mock):
    repo = UserRepository("UsersTable")
    user_id = "12345"
    repo.create({"user_id": user_id, "username": "original", "email": "o@test.com", "edad": 20})
    update_data = UserUpdate(edad=25)
    
    clean_update = update_data.model_dump(exclude_none=True) 
    repo.update(user_id, clean_update)

    updated_user = repo.get(user_id)
    assert updated_user["edad"] == 25           
    assert updated_user["username"] == "original"