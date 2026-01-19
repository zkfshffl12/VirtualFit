from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

    new_user = models.User(
        email=user.email,
        hashed_password=user.password,  # 해시태그 미적용
        nickname=user.nickname
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user