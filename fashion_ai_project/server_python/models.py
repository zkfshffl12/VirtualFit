from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence
from sqlalchemy.sql import func
from database import Base

# 유저 테이블
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('USER_ID_SEQ', quote=False), primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    nickname = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# 2. 옷장 테이블 (이미지 정보)
class Clothes(Base):
    __tablename__ = "clothes"

    id = Column(Integer, Sequence('CLOTHES_ID_SEQ', quote=False), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # 어떤 유저의 옷인지 연결
    image_url = Column(String(300), nullable=False)  # static 폴더 내의 파일 경로
    category = Column(String(50))  # 상의, 하의, 아우터 등
    created_at = Column(DateTime(timezone=True), server_default=func.now())