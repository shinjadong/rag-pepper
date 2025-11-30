# 1인 개발자를 위한 개인화 RAG 시스템 완벽 가이드

**월 7만원 이하로 "세팅 후 잊어버려도 되는" AI 지식 서버 구축법**—Obsidian과 Notion 데이터를 통합하여 Claude, ChatGPT, Cursor가 모두 연결할 수 있는 MCP 기반 개인 RAG 서버를 만드는 방법을 제시합니다. 핵심은 **n8n 셀프호스팅 + Supabase pgvector + FastMCP**의 조합으로, 초기 셋업 약 8시간 투자 후 월 $15 미만으로 운영 가능합니다.

---

## Vector DB 선택: Supabase와 Qdrant가 압도적 승자

1인 사용자 기준(~10,000개 문서, 일 50-100회 쿼리)에서 **Supabase pgvector**와 **Qdrant Cloud**가 가장 합리적인 선택입니다. Pinecone은 2024년 9월 이후 **최소 월 $50** 정책으로 개인 사용자에게 과도한 비용이 됐습니다.

| Vector DB | 무료 티어 | 10K 벡터 비용 | MCP 지원 | 추천도 |
|-----------|----------|--------------|---------|-------|
| **Supabase** | 500MB (무제한 API) | **$0-25/월** | ✅ 공식 서버 | ⭐⭐⭐⭐⭐ |
| **Qdrant Cloud** | 1GB 영구 무료 | **$0-9/월** | ✅ 공식 서버 | ⭐⭐⭐⭐⭐ |
| Pinecone | 2GB/1M reads | $50/월 최소 | ✅ MindsDB 경유 | ⭐⭐ |
| Weaviate | 14일 샌드박스 | $25-50/월 | 커뮤니티 | ⭐⭐⭐ |
| Chroma | $5 크레딧 | $3-5/월 | 커뮤니티 | ⭐⭐⭐ |

**Supabase**는 PostgreSQL 기반이라 SQL에 익숙한 개발자에게 디버깅이 쉽고, 대시보드로 데이터를 직접 확인할 수 있습니다. **Qdrant**는 벤치마크 성능이 가장 뛰어나고 공식 MCP 서버(`mcp-server-qdrant`)가 잘 관리됩니다. 둘 다 무료 티어로 10,000개 문서는 충분히 처리합니다.

**숨겨진 함정**: Supabase 무료 티어는 1주일 비활성 시 프로젝트가 일시정지됩니다. 정기적 쿼리가 있으면 문제없지만, Pro 플랜($25/월)으로 이 제한을 해제할 수 있습니다.

---

## ETL 파이프라인: n8n 셀프호스팅이 유일한 정답

Obsidian의 **로컬 파일 변경 감지**가 필수 요구사항이므로, 선택지가 크게 좁혀집니다. n8n Cloud, Make, Zapier는 모두 로컬 폴더를 감시할 수 없습니다. 오직 **n8n 셀프호스팅**만이 Local File Trigger 노드를 제공합니다.

```
┌─────────────────────────────────────────────────────────────────┐
│  n8n 셀프호스팅 ($5-10/월 VPS)                                    │
├─────────────────────────────────────────────────────────────────┤
│  Obsidian Vault                                                  │
│       ↓ Local File Trigger (실시간)                              │
│  ────────────────────────────────────────                       │
│  Notion Database                                                 │
│       ↓ Schedule Trigger (매시간)                                │
│  ────────────────────────────────────────                       │
│       ↓ Text Splitter → OpenAI Embeddings → Supabase/Qdrant     │
└─────────────────────────────────────────────────────────────────┘
```

n8n은 **RAG 스타터 템플릿**을 제공하고, Notion 노드에서 `last_edited_time` 필터로 증분 업데이트가 가능합니다. 월 **$5-10의 VPS**(DigitalOcean, Hetzner)에서 무제한 실행이 가능하므로, n8n Cloud($20/월)보다 경제적이면서 기능도 더 풍부합니다.

**대안으로 LangChain + watchdog** 조합도 가능하지만, 외부 스케줄러(cron) 설정이 필요하고 시각적 디버깅이 어렵습니다. ADHD 성향의 사용자라면 문제 발생 시 n8n의 비주얼 워크플로우가 훨씬 직관적입니다.

---

## RAG 오케스트레이션과 MCP 서버 구축

### Dify vs Flowise vs 직접 구축

| 플랫폼 | API 노출 | MCP 지원 | Vector DB | 셋업 시간 | 추천 상황 |
|-------|---------|---------|-----------|---------|----------|
| **Dify** | ✅ 원클릭 | ✅ 양방향 네이티브 | Weaviate, Qdrant 등 | 1-2시간 | 빠른 프로토타이핑 |
| **Flowise** | ✅ 자동 생성 | ✅ 노드/래퍼 | **18+ DB 지원** | 30분-1시간 | Vector DB 유연성 |
| **FastMCP 직접 구축** | ✅ 완전 제어 | ✅ 네이티브 | 모든 DB | 2-4시간 | 최소 의존성 |

**Dify**는 v1.6.0부터 양방향 MCP를 네이티브 지원합니다—MCP 서버를 도구로 사용하거나, Dify 앱을 MCP 서버로 노출할 수 있습니다. 그러나 Pinecone이 지원되지 않고, 셀프호스팅 시 리소스 요구량이 높습니다.

**Flowise**는 LangChain 기반으로 **18개 이상의 Vector DB**를 지원하며, LEGO 블록처럼 직관적인 인터페이스가 장점입니다. 다만 MCP 서버로의 직접 노출은 래퍼가 필요합니다.

**FastMCP 직접 구축**이 실제로 가장 간단한 경로일 수 있습니다. Python 데코레이터 몇 개로 완전한 MCP 서버를 만들 수 있습니다:

```python
from mcp.server.fastmcp import FastMCP
from supabase import create_client

mcp = FastMCP("Personal RAG")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@mcp.tool()
def fetch_context(query: str, top_k: int = 5) -> str:
    """개인 지식베이스에서 관련 문맥을 검색합니다."""
    response = supabase.rpc('match_documents', {
        'query_embedding': get_embedding(query),
        'match_count': top_k
    }).execute()
    return format_results(response.data)

if __name__ == "__main__":
    mcp.run(transport='stdio')
```

---

## MCP 프로토콜 호환성 완전 정리

MCP(Model Context Protocol)는 2024년 11월 Anthropic이 발표한 개방형 표준으로, "AI 앱을 위한 USB-C"라고 불립니다. 현재 **Claude, ChatGPT, Cursor** 모두 MCP를 지원합니다.

### Claude Desktop 연결

`~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "personal-rag": {
      "command": "python",
      "args": ["/path/to/rag_server.py"],
      "env": {
        "SUPABASE_URL": "your-url",
        "SUPABASE_KEY": "your-key"
      }
    }
  }
}
```

### ChatGPT 연결

ChatGPT는 **원격 서버만** 지원합니다(localhost 불가). Developer Mode(Pro/Plus 플랜)에서 Settings → Connectors → Advanced에서 MCP 서버 URL을 등록합니다. Cloudflare Workers나 Railway에 배포된 HTTP/SSE 엔드포인트가 필요합니다.

### Cursor AI 연결

`~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "personal-rag": {
      "command": "uv",
      "args": ["run", "rag_server.py"]
    }
  }
}
```

**핵심 인사이트**: Claude Desktop과 Cursor는 로컬 stdio 서버를 지원하므로 추가 비용 없이 연결됩니다. ChatGPT를 위해서는 별도 호스팅이 필요하지만, 무료 티어(Railway, Render)로 가능합니다.

---

## 실제 구현 가능한 3가지 아키텍처 시나리오

### 시나리오 A: 최소 비용 로컬 우선 ($5-15/월)

```
┌──────────────────────────────────────────────────────────────┐
│  Obsidian Vault (로컬)                                        │
│       ↓ watchdog Python 스크립트                              │
│  Notion → n8n 셀프호스팅 (Hetzner $5/월)                       │
│       ↓                                                       │
│  OpenAI text-embedding-3-small ($0.02/1M tokens)              │
│       ↓                                                       │
│  Supabase pgvector (무료 티어)                                │
│       ↓                                                       │
│  FastMCP 서버 (동일 VPS)                                      │
│       ↓                                                       │
│  Claude Desktop / Cursor (로컬 stdio)                         │
└──────────────────────────────────────────────────────────────┘
```

| 항목 | 월 비용 |
|-----|--------|
| VPS (n8n + MCP 서버) | $5-10 |
| Supabase | $0 (무료) |
| OpenAI Embedding (10K docs 초기 + 일 50개 업데이트) | ~$2-5 |
| **총합** | **$7-15** |

**셋업 난이도**: 중간 (6-8시간)
**유지보수**: 월 1회 VPS 업데이트 확인
**장점**: 최소 비용, 데이터 완전 제어
**단점**: ChatGPT 연결 시 추가 작업 필요

---

### 시나리오 B: 균형잡힌 매니지드 서비스 ($25-40/월)

```
┌──────────────────────────────────────────────────────────────┐
│  Obsidian Vault (Dropbox 동기화)                              │
│       ↓ Dropbox webhook → n8n Cloud                          │
│  Notion → n8n Cloud Starter ($20/월)                          │
│       ↓                                                       │
│  OpenAI text-embedding-3-small                                │
│       ↓                                                       │
│  Supabase Pro ($25/월) - 프로젝트 일시정지 방지               │
│       ↓                                                       │
│  Flowise Cloud Free (2 flows)                                 │
│       ↓ REST API                                              │
│  Claude/ChatGPT/Cursor (Custom GPT Actions, MCP)              │
└──────────────────────────────────────────────────────────────┘
```

| 항목 | 월 비용 |
|-----|--------|
| n8n Cloud Starter | $20 |
| Supabase Pro | $25 |
| OpenAI Embedding | ~$2-5 |
| Flowise Cloud | $0 (무료 티어) |
| **총합** | **$47-50** ⚠️ 예산 초과 |

**주의**: 이 시나리오는 $70 예산을 약간 초과합니다. 비용을 맞추려면 Supabase 무료 티어를 유지하고 정기 쿼리로 일시정지를 방지하세요.

**셋업 난이도**: 낮음 (3-4시간)
**유지보수**: 거의 없음 (완전 매니지드)
**장점**: 서버 관리 제로
**단점**: Obsidian 로컬 파일 트리거 불가 (클라우드 동기화 필수)

---

### 시나리오 C: 완전 로컬 프라이버시 우선 ($0/월 + 초기 투자)

```
┌──────────────────────────────────────────────────────────────┐
│  Obsidian Vault                                               │
│       ↓ chokidar/watchdog                                     │
│  Notion Export (수동 또는 스크립트)                            │
│       ↓                                                       │
│  Ollama nomic-embed-text (로컬 임베딩)                        │
│       ↓                                                       │
│  LanceDB (파일 기반 Vector DB)                                │
│       ↓                                                       │
│  FastMCP 서버 (로컬)                                          │
│       ↓                                                       │
│  Claude Desktop / Cursor                                      │
└──────────────────────────────────────────────────────────────┘
```

| 항목 | 월 비용 |
|-----|--------|
| 모든 것 로컬 | **$0** |
| 초기 하드웨어 요구: 16GB+ RAM, SSD | 기존 장비 활용 |

**셋업 난이도**: 높음 (8-12시간)
**유지보수**: Ollama/모델 업데이트 시 수동 관리
**장점**: 완전한 프라이버시, API 비용 제로
**단점**: ChatGPT 연결 불가, Notion 실시간 동기화 어려움, 임베딩 품질이 OpenAI보다 낮을 수 있음

---

## Obsidian 동기화: 플러그인 vs 커스텀 솔루션

### 기존 플러그인의 한계

**Smart Connections**와 **Obsidian Copilot**은 로컬 벡터 DB를 생성하지만, **외부 Vector DB로 푸시할 수 없습니다**. 내부 사용 전용으로 설계됐습니다.

다만 `smart-connections-mcp` 프로젝트가 있어 Smart Connections의 로컬 벡터 DB를 MCP 서버로 노출할 수 있습니다—추가 Vector DB 없이 바로 Claude Desktop에서 사용 가능합니다.

### 권장 동기화 전략

```python
# obsidian_sync.py - watchdog 기반 실시간 동기화
import frontmatter
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VaultHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.md'):
            # 1. 기존 임베딩 삭제 (filepath 메타데이터 기준)
            vector_db.delete(filter={'filepath': event.src_path})
            
            # 2. 프론트매터 + 태그 + 링크 추출
            with open(event.src_path) as f:
                post = frontmatter.load(f)
            metadata = extract_metadata(post)
            
            # 3. 마크다운 헤더 기준 청킹 (400-500 토큰)
            chunks = markdown_splitter.split(post.content)
            
            # 4. 임베딩 생성 및 저장
            for chunk in chunks:
                embedding = embeddings.embed(chunk)
                vector_db.upsert(chunk, embedding, metadata)
```

**청킹 전략**: 마크다운 헤더(#, ##, ###)를 기준으로 먼저 분할하고, 큰 섹션은 400-500 토큰으로 재분할합니다. 50-100 토큰 오버랩을 주면 문맥 손실을 방지합니다.

---

## Notion 동기화: 증분 업데이트가 핵심

Notion은 웹훅을 제한적으로 지원하므로, **폴링 + `last_edited_time` 필터**가 표준 접근법입니다.

```python
# n8n 워크플로우 또는 Python 스크립트
def sync_notion_incremental():
    last_sync = load_last_sync_timestamp()
    
    pages = notion.databases.query(
        database_id=DB_ID,
        filter={
            "timestamp": "last_edited_time",
            "last_edited_time": {"on_or_after": last_sync}
        }
    )
    
    for page in pages['results']:
        content = extract_all_blocks(page['id'])
        content_hash = md5(content)
        
        # 내용이 실제로 변경된 경우만 재임베딩
        if cached_hash.get(page['id']) != content_hash:
            process_and_embed(page, content)
            cached_hash[page['id']] = content_hash
    
    save_last_sync_timestamp(now())
```

**주의점**: Notion API의 `last_edited_time`은 분 단위로만 정확합니다. 매시간 폴링이면 충분하고, 레이트 리밋(~3 req/sec)에 주의하세요.

---

## 커뮤니티 검증 결과와 피해야 할 함정

### 실제로 "살아남은" 스택

Reddit r/LocalLLaMA, Hacker News, GitHub에서 2024-2025년 실사용자들이 지속적으로 사용하는 검증된 조합:

1. **Reor** - "고엔트로피 사람들을 위한" 명시적 설계, ADHD 친화적
2. **Khoj** - Obsidian 플러그인 + 셀프호스팅 조합, 활발한 개발
3. **Obsidian + Ollama + Copilot** - 가장 오래 검증된 조합

### 피해야 할 함정

**"데이터가 많을수록 정확도가 낮아진다"**—가장 많이 보고되는 문제입니다. 커뮤니티 합의는 **선별적 임베딩**입니다. 전체 Vault가 아니라 관련 노트만 선택적으로 임베딩하면 더 좋은 결과를 얻습니다.

**작은 모델은 불충분합니다.** 8B 파라미터가 최소이고, 신뢰할 수 있는 엔티티 추출에는 32B+ 모델이 권장됩니다. 로컬 RAG를 원한다면 최소 16GB RAM이 필요합니다.

**복잡한 파이프라인은 방치됩니다.** 초기 열정이 식으면 유지보수가 안 됩니다. "세팅 후 잊어버려도 되는" 단순한 구조가 장기적으로 생존합니다.

---

## 임베딩 모델 비용 비교

| 모델 | 비용 (1M 토큰) | 차원 | 품질 | 추천 |
|-----|--------------|-----|-----|-----|
| **OpenAI text-embedding-3-small** | $0.02 | 1536 | 우수 | ⭐ 가성비 최고 |
| OpenAI text-embedding-3-large | $0.13 | 3072 | 최상 | 고품질 필요시 |
| Cohere embed-english-v3 | $0.10 | 1024 | 우수 | OpenAI 대안 |
| **Ollama nomic-embed-text** | $0 (로컬) | 768 | 양호 | 완전 무료 |

**10,000개 문서(평균 500토큰) 초기 임베딩 비용**:
- text-embedding-3-small: 약 $0.10
- 일 50개 문서 업데이트(월 1,500개): 약 $0.015/월

임베딩 비용은 무시해도 될 수준입니다. **$70 예산의 대부분은 인프라(VPS, 매니지드 서비스)에 할당**하세요.

---

## 원픽(One Pick) 추천: 최적의 단일 스택

### 🏆 권장 구성

| 구성요소 | 선택 | 이유 |
|---------|-----|-----|
| **Vector DB** | Supabase pgvector | 무료 티어, SQL 친숙, 대시보드 |
| **ETL** | n8n 셀프호스팅 | 로컬 파일 트리거, 무제한 실행 |
| **임베딩** | OpenAI text-embedding-3-small | 가성비, 안정성 |
| **MCP 서버** | FastMCP Python | 최소 코드, 완전 제어 |
| **호스팅** | Hetzner VPS (CX22) | $5/월, 유럽 서버 |

### 월 예상 비용

| 항목 | 비용 |
|-----|-----|
| Hetzner VPS (n8n + MCP 서버) | €4.49 (~$5) |
| Supabase | $0 |
| OpenAI Embedding | ~$2-5 |
| **총합** | **$7-10/월** ✅ |

### 초기 셋업 예상 시간

1. Supabase 프로젝트 생성 + pgvector 활성화: **30분**
2. Hetzner VPS 생성 + Docker 설치: **1시간**
3. n8n Docker 배포 + Obsidian/Notion 워크플로우: **2-3시간**
4. FastMCP 서버 코드 작성 + 테스트: **2시간**
5. Claude Desktop/Cursor MCP 설정: **30분**
6. 전체 테스트 및 디버깅: **1-2시간**

**총 예상 시간: 7-9시간** (주말 하루 프로젝트)

### 주의사항 및 함정

1. **Supabase 무료 티어 일시정지**: n8n에서 매일 쿼리를 실행하면 방지됩니다
2. **n8n Docker macOS 이슈**: Local File Trigger가 macOS Docker에서 간헐적 문제—Linux VPS 권장
3. **ChatGPT 연결**: 별도의 원격 MCP 엔드포인트 필요 (Railway 무료 티어로 해결 가능)
4. **대용량 파일**: 10MB+ 파일은 청킹 전 별도 처리 필요
5. **Notion 레이트 리밋**: 대량 초기 임포트 시 지수 백오프 구현 필요

### 확장 경로

현재 스택은 프론티어 모델 교체에 완전히 독립적입니다:
- GPT-5, Claude 4 출시 시: MCP 서버 코드 변경 없음
- 데이터 증가 시: Supabase Pro($25/월)로 업그레이드
- 더 많은 소스 추가: n8n 워크플로우만 추가

**이 아키텍처는 "데이터 파이프라인은 고정, 프론트엔드(AI 모델)만 교체"라는 원칙을 완벽히 구현합니다.**

---

## 빠른 시작 체크리스트

```
□ 1. Supabase 계정 생성 → pgvector 확장 활성화
□ 2. Hetzner VPS 생성 (CX22, €4.49/월)
□ 3. Docker + n8n 설치: docker run -d n8nio/n8n
□ 4. n8n에서 Obsidian 워크플로우 생성 (Local File Trigger → Embeddings → Supabase)
□ 5. n8n에서 Notion 워크플로우 생성 (Schedule → Notion Query → Embeddings → Supabase)
□ 6. FastMCP 서버 스크립트 작성 (fetch_context 함수)
□ 7. Claude Desktop config.json에 MCP 서버 등록
□ 8. "내 Obsidian 노트에서 X에 대해 찾아줘" 테스트
□ 9. Cursor .cursor/mcp.json에도 등록 (선택)
```

이 가이드를 따르면 **월 $10 미만**으로 모든 최신 AI 서비스가 자유롭게 접근하는 개인화된 지식 서버를 구축할 수 있습니다. 한번 세팅하면 새 노트를 작성할 때마다 자동으로 인덱싱되고, Claude에게 "내 사업 계획서에서 경쟁사 분석 부분 찾아줘"라고 말하면 즉시 관련 문맥을 가져옵니다.