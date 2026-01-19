from database import engine

# Oracle Sequence 생성
with engine.connect() as conn:
    try:
        conn.execute("CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1")
        print("✅ user_id_seq 생성 완료")
    except Exception as e:
        print(f"user_id_seq: {e}")
    
    try:
        conn.execute("CREATE SEQUENCE clothes_id_seq START WITH 1 INCREMENT BY 1")
        print("✅ clothes_id_seq 생성 완료")
    except Exception as e:
        print(f"clothes_id_seq: {e}")
    
    conn.commit()

print("\n✅ 모든 Sequence 생성이 완료되었습니다!")
