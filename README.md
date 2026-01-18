# VirtualFit
fashion_ai_project/             # 전체 루트 폴더
│
├── app_flutter/                # [프론트엔드] Flutter 안드로이드 앱
│   ├── android/                # 안드로이드 네이티브 설정
│   ├── assets/                 # 이미지, 아이콘, 폰트
│   │   └── images/             # 기본 아바타 모델 등
│   ├── lib/                    # 다트 코딩의 핵심
│   │   ├── main.dart           # 앱 실행 시작점
│   │   ├── models/             # User, Cloth 데이터 모델
│   │   ├── screens/            # UI 화면 (Login, Closet, Avatar, Home)
│   │   ├── services/           # API 통신 (HTTP 요청), Firebase 연동
│   │   └── widgets/            # 공통 버튼, 옷 카드 아이템 등
│   └── pubspec.yaml            # 라이브러리 설정 (dio, image_picker 등)
│
├── server_python/              # [백엔드] FastAPI 서버
│   ├── main.py                 # 서버 통합 및 실행 (Uvicorn)
│   ├── database.py             # DB 연결 및 세션 설정
│   ├── models.py               # DB 테이블 정의 (SQLAlchemy)
│   ├── schemas.py              # 데이터 검증 (Pydantic)
│   ├── api/                    # 기능별 API 라우터
│   │   ├── auth.py             # 로그인/계정 관련
│   │   └── clothes.py          # 옷 등록/배경 제거/추천 로직
│   ├── core/                   # 핵심 알고리즘
│   │   ├── ai_logic.py         # rembg 활용 배경 제거 함수
│   │   └── coordinator.py      # 날씨 기반 코디 추천 엔진
│   ├── static/                 # 배경 지운 옷 사진 보관 폴더 (PNG)
->  코디 커스터마이징

<구독여부 확인 후>
│   ├── .env                    # 환경변수 (DB 비번, 날씨 API 키)
│   └── requirements.txt        # 설치 리스트 (fastapi, rembg 등)
│
└── docs/

