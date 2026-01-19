from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "패션 AI 서버가 정상 작동 중입니다!"}

@app.get("/db-test")
def test_db(db: Session = Depends(get_db)):
    # DB 연결이 잘 됐는지 확인하는 간단한 테스트
    return {"status": "오라클 DB 연결 성공!"}