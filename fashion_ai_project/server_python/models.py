from sqlalchemy import column, integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

# 유저 테이블
class user(Base):
    __tablename__="users"

id=column(Integer, primary_key=True, index=True)
email=column(String(100), unique=True, index=True, nullable=False)
hashed_password=column(String(200), nullable=False)
nickname=column(String(50))
created_at=column(DateTime(timezone=True), servaer_default=func.now())

# 2. 옷장 테이블 (이미지 정보)
class clothes(Base):
    __tablename__ = "clothes"

id = column(Integer, primary_key=True, index=True)
user_id=column(Integer, ForeignKey("users.id")) # 어떤 유저의 옷인지 연결
import_user=column(String(300), nullable=False) # static 폴더 내의 파일 경로
category=column(String(50))                     # 상의, 하의, 아우터 등
created_at=column(DateTime(timezone=True), server_default=func.now())