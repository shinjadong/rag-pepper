---
title: "Error Types"
source: "https://docs.dify.ai/en/use-dify/debug/error-type"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
[Skip to main content](https://docs.dify.ai/en/use-dify/debug/#content-area)

Each node type throws specific error classes that help you understand what went wrong and how to fix it.

## Node-specific errors

- Code
- LLM
- HTTP Request
- Tool

`CodeNodeError`

Your Python or JavaScript code threw an exception during execution

![Code Error](https://assets-docs.dify.ai/2024/12/c86b11af7f92368180ea1bac38d77083.png)

Code Error

`OutputValidationError`

The data type your code returned doesn’t match the output variable type you configured

`DepthLimitError`

Your code created nested data structures deeper than 5 levels

`CodeExecutionError`

The sandbox service couldn’t execute your code - usually means the service is down

![](https://assets-docs.dify.ai/2024/12/ab8cae01a590b037017dfe9ea4dbbb8b.png)

## System-level errors

`InvokeConnectionError`

Network connection failed to the external service

`InvokeServerUnavailableError`

External service returned a 503 status or is temporarily down

`InvokeRateLimitError`

You’ve hit rate limits on the API or model provider

`QuotaExceededError`

Your usage quota has been exceeded for this service

Was this page helpful?

[Previous](https://docs.dify.ai/en/use-dify/debug/history-and-logs)[Overview](https://docs.dify.ai/en/use-dify/publish/README)

[

Next

](https://docs.dify.ai/en/use-dify/publish/README)