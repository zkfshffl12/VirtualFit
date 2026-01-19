from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
import models, schemas
from core.security import get_password_hash
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import jwt
import os

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# JWT 설정
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.get("/")
def read_root():
    return {"message": "패션 AI 서버가 정상 작동 중입니다!"}

@app.get("/db-test")
def test_db(db: Session = Depends(get_db)):
    # DB 연결이 잘 됐는지 확인하는 간단한 테스트
    return {"status": "오라클 DB 연결 성공!"}

@app.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 이미 가입된 이메일 확인
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 가입된 이메일입니다.")
    
    hashed_password = get_password_hash(user.password)

    new_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        nickname=user.nickname
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login", response_model=schemas.Token)
def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    # 1. DB에서 해당 이메일 유저 찾기
    user = db.query(models.User).filter(models.User.email == user_data.email).first()

    # 2. 유저가 없거나 비밀번호가 틀리면 에러 반환
    if not user or user.hashed_password != user_data.password:
        raise HTTPException(status_code=400, detail="이메일 혹은 비밀번호가 틀렸습니다.")
    
    # 3. 토큰 생성
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"} 
