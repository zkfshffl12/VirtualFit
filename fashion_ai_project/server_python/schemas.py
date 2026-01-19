from pydantic import BaseModel, EmailStr
from typing import Optional

# 회원데이터 받기
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    nickname: Optional[str] = None

# 회원데이터 응답
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    nickname: Optional[str]

    class Config:
        from_attributes = True