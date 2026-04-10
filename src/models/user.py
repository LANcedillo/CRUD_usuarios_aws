from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4

# Modelo base para evitar repetición
class UserBase(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=20)
    email: Optional[EmailStr] = None
    edad: Optional[int] = Field(None, ge=18)

class UserCreate(UserBase):
    # En la creación, estos campos SÍ son obligatorios
    username: str = Field(None, min_length=3, max_length=20)
    email: EmailStr
    edad: int = Field(None, ge=18)

class UserUpdate(UserBase):
    # Aquí todo es opcional. El usuario puede enviar solo 1 campo o todos.
    pass
    
class UserResponse(UserCreate):
    # Este modelo se usa para lo que sale de la base de datos
    user_id: UUID = Field(default_factory=uuid4)
    status: str = "PENDING"