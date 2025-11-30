---
title: "Knowledge Retrieval"
source: "https://docs.dify.ai/en/use-dify/nodes/knowledge-retrieval"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Search knowledge bases for relevant information"
tags:
  - "clippings"
---
The Knowledge Retrieval node searches your knowledge bases for relevant information and returns contextual content for use in downstream nodes. It enables RAG (Retrieval-Augmented Generation) applications by providing specific information from your documents.

![Knowledge Retrieval Node Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d90961c6d794d425a8e11df177315188.png)

Knowledge Retrieval Node Interface

Knowledge Retrieval node configuration

Create and populate knowledge bases before using this node. See the [knowledge base creation guide](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/introduction) for setup instructions.

## Configuration

### Query and Knowledge Base Selection

The **Query** determines what to search for in your knowledge bases. Use `sys.query` for user input in chatflow applications, or any text variable from your workflow. Queries are limited to 200 characters.Select one or more **Knowledge Bases** to search. Each contains indexed documents you’ve uploaded to Dify. Multiple knowledge bases can be searched simultaneously using different strategies.

### Retrieval Strategy

Choose how to search your content:

## Advanced Settings

![Knowledge retrieval configuration interface](https://assets-docs.dify.ai/2025/03/fbd43d558f83b355a1b18ac26a253b84.png)

Knowledge retrieval configuration interface

Advanced retrieval configuration options

### Retrieval Parameters

**Top K** controls how many document chunks to retrieve. Start with 3-5 chunks for focused results or 10-15 for comprehensive coverage.**Score Threshold** sets minimum similarity scores. Higher thresholds (0.7+) ensure relevance, lower thresholds (0.5-) include more tangential content.**Reranking** re-scores results after initial retrieval. Enable for hybrid search, many chunks, or when precision matters more than speed.Filter results using document metadata like type, date, or department. Set up metadata when uploading documents to enable targeted searching in large knowledge bases.

### Multi-Knowledge Base Strategies

**N-to-1 Recall** uses function calling to analyze queries, select appropriate knowledge bases, and optimize searches. Best for specialized knowledge bases in different domains.**Multi-way Recall** queries all selected knowledge bases simultaneously and combines results. Use when information spans multiple sources or you need comprehensive coverage.

![Retrieval Mode Comparison](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/4a3007cda9dfa50ddac3711693725dce.png)

Retrieval Mode Comparison

Comparison of retrieval strategies for multiple knowledge bases

## Output and Integration

The node outputs an array of retrieved document chunks containing text content and metadata (source, score, document ID). This structured output preserves information needed for citations.

### RAG Integration

Connect Knowledge Retrieval output to LLM node context inputs for RAG applications. When using retrieval results as context variables, Dify automatically tracks sources and enables citations.

```
System: Answer based on the provided context.

Context: {{knowledge_retrieval.result}}

User: {{user_question}}
```

### Rate Limiting

Knowledge retrieval operations are subject to rate limits based on your subscription plan. The system tracks requests using Redis with a 60-second sliding window. When limits are exceeded, a `RateLimitExceeded` error is returned.

### Performance Considerations

Retrieval quality depends on indexing practices. Smaller chunks (200-500 tokens) enable precise retrieval, larger chunks (800-1500 tokens) maintain context. Knowledge bases have rate limits - the node handles throttling and caches identical queries automatically.

[Previous](https://docs.dify.ai/en/use-dify/nodes/llm)[Answer](https://docs.dify.ai/en/use-dify/nodes/answer)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/answer)