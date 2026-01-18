# VirtualFit

AI 기반 패션 코디 추천 애플리케이션

## 📋 프로젝트 개요

VirtualFit은 AI 기술을 활용하여 사용자의 옷장을 관리하고, 날씨와 상황에 맞는 최적의 코디를 추천하는 스마트 패션 애플리케이션입니다.

## 🎯 주요 기능

- 📸 **옷 이미지 업로드 & 배경 제거** (AI 활용)
- 👔 **AI 자동 코디 추천** (날씨 기반)
- 🎨 **커스텀 코디 생성** (프리미엄)
- 💳 **구독 결제 시스템**
- ☁️ **날씨 연동 코디 추천**

## 🛠 기술 스택

### Frontend
- **Flutter** - 크로스 플랫폼 모바일 앱
- **Dart** - Flutter 개발 언어
- **Provider** - 상태 관리

### Backend
- **FastAPI** - Python 웹 프레임워크
- **SQLAlchemy** - ORM
- **Oracle Database** - 데이터베이스
- **rembg** - AI 배경 제거

### AI/ML
- **rembg** - 이미지 배경 제거
- **날씨 API** - 날씨 기반 추천

## 📁 프로젝트 구조

```
fashion_ai_project/
│
├── app_flutter/              # Flutter 모바일 앱
│   ├── android/              # 안드로이드 설정
│   ├── assets/images/        # 이미지 리소스
│   ├── lib/
│   │   ├── main.dart         # 앱 진입점
│   │   ├── models/           # 데이터 모델
│   │   ├── screens/          # UI 화면
│   │   ├── services/         # API 통신
│   │   └── widgets/          # 재사용 위젯
│   └── pubspec.yaml          # 의존성 관리
│
├── server_python/            # FastAPI 백엔드
│   ├── main.py               # 서버 진입점
│   ├── database.py           # DB 연결
│   ├── models.py             # DB 모델
│   ├── schemas.py            # 데이터 검증
│   ├── api/
│   │   ├── auth.py           # 인증 API
│   │   └── clothes.py        # 옷장 API
│   ├── core/
│   │   ├── ai_logic.py       # AI 배경 제거
│   │   └── coordinator.py    # 코디 추천 엔진
│   ├── static/               # 업로드 이미지
│   ├── .env                  # 환경 변수
│   └── requirements.txt      # Python 패키지
│
└── docs/                     # 프로젝트 문서
```

## 🚀 시작하기

### Backend 실행

```bash
cd fashion_ai_project/server_python
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend 실행

```bash
cd fashion_ai_project/app_flutter
flutter pub get
flutter run
```

## 📝 API 엔드포인트

- `GET /` - 서버 상태 확인
- `GET /test` - DB 연결 테스트
- `POST /api/auth/login` - 로그인
- `POST /api/clothes/upload` - 옷 업로드
- `GET /api/clothes/` - 옷장 조회
- `POST /api/coordi/generate` - AI 코디 생성

## 💾 데이터베이스

Oracle Database를 사용하며, 주요 테이블:
- `users` - 사용자 정보
- `clothes` - 옷 정보
- `coordis` - 코디 정보
- `subscriptions` - 구독 정보

## 📄 라이선스

MIT License

