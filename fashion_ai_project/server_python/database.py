from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# 오라클 엔진 시동!
engine = create_engine(settings.DATABASE_URL, echo=True)

# 데이터베이스와 대화할 세션 만들기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테이블을 만들 때 기준이 되는 기본 클래스
Base = declarative_base()

# DB 연결을 도와주는 스니펫
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()