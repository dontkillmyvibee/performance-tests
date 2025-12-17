from pydantic import BaseModel, EmailStr


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя (POST /api/v1/users).
    """
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UserSchema(CreateUserRequestSchema):
    """
    Схема данных пользователя (включая идентификатор пользователя).
    """
    id: str


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на создание пользователя (POST /api/v1/users).
    """
    user: UserSchema
