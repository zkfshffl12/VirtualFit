from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from sqlalchemy.orm import Session
from database import get_db
import models

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(OAuth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="인증 정보가 유효하지 않습니다",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload + jwt.decode(token, os.getenv("SECRET_KEY"), algorithems=("ALGORITHM",))
        email: str =payload.get*("sub")
        if emaill is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

#유저확인 용
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user
