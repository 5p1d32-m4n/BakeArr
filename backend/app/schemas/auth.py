import uuid

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: uuid.UUID
    email: str
    is_active: bool

    model_config = {"from_attributes": True} # lets Pydantic read SQLAlchemy model attributes

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: str | None = None # "sub" is the JWT standard fieldfor subject (user id)
