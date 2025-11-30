# RAG Pepper

**Personal RAG System for Solo Developers**

Obsidian 노트를 활용한 개인화된 RAG(Retrieval-Augmented Generation) 시스템입니다.
Claude Desktop에서 MCP를 통해 내 노트를 직접 검색하고 질의할 수 있습니다.

## Architecture

```
Obsidian (로컬 Markdown)
     |
     v
   n8n (Self-hosted) -----> 파일 변경 감지 & ETL
     |
     v
Supabase (Cloud) <--------- pgvector로 벡터 저장
     |
     v
  Dify (Self-hosted) <----- RAG 오케스트레이션 & LLM 연동
     |
     v
MCP Server --------------> Claude Desktop 연결
```

## Quick Start

### 1. 환경 설정

```bash
# .env 파일 생성
cp .env.example .env

# 필수 값 설정
# - SECRET_KEY: `openssl rand -base64 42`로 생성
# - SUPABASE_URL / SUPABASE_API_KEY
# - OPENAI_API_KEY
# - OBSIDIAN_VAULT_PATH
```

### 2. Docker Compose 실행

```bash
cd infrastructure
docker compose up -d
```

### 3. 서비스 접속

- **Dify**: http://localhost (초기 설정: `/install`)
- **n8n**: http://localhost:5678

### 4. MCP 서버 설정 (Claude Desktop)

```bash
cd mcp-server
pip install -r requirements.txt

# Claude Desktop 설정에 추가
# 참조: mcp-server/claude_desktop_config.example.json
```

## Project Structure

```
rag-pepper/
├── infrastructure/          # Docker Compose 및 설정
│   ├── docker-compose.yaml  # Dify + n8n 통합 설정
│   └── nginx/               # Nginx 리버스 프록시 설정
├── mcp-server/              # Claude Desktop용 MCP 서버
│   ├── main.py              # MCP 서버 메인 코드
│   └── requirements.txt     # Python 의존성
├── n8n/
│   └── workflows/           # n8n 워크플로우 템플릿
├── docs/
│   ├── chat-logs/           # 프로젝트 대화 로그
│   └── dev-docs/            # 개발 참조 문서
├── .env.example             # 환경 변수 템플릿
└── README.md
```

## Key Features

- **Set & Forget**: 한 번 설정하면 자동으로 동기화
- **월 $70 이하 유지비용**: 클라우드 의존성 최소화
- **Claude Desktop 통합**: MCP를 통한 네이티브 연동

## Services

| Service | Port | Description |
|---------|------|-------------|
| Dify Web | 80 | RAG 애플리케이션 UI |
| Dify API | 80/v1 | Service API |
| n8n | 5678 | 워크플로우 자동화 |
| PostgreSQL | 5432 | Dify 내부 DB |
| Redis | 6379 | 캐시 & 큐 |

## License

MIT
