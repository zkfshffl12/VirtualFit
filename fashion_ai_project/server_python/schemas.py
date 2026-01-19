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

# 로그인 요청
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# 토큰 응답
class Token(BaseModel):
    access_token: str
    token_type: str