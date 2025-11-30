---
title: "HTTP Request"
source: "https://docs.dify.ai/en/use-dify/nodes/http-request"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Connect to external APIs and web services"
tags:
  - "clippings"
---
The HTTP Request node connects your workflow to external APIs and web services. Use it to fetch data, send webhooks, upload files, or integrate with any service that accepts HTTP requests.

![HTTP Request node interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/07c5e952eb4c9d6a32d0b7c2d855d4a5.png)

HTTP Request node interface

HTTP Request node configuration

## HTTP Methods

The node supports all standard HTTP methods for different types of operations:

## Configuration

Configure every aspect of your HTTP request including URL, headers, query parameters, request body, and authentication. Variables from previous workflow nodes can be dynamically inserted anywhere in your request configuration.

### Variable Substitution

Reference workflow variables using double curly braces: `{{variable_name}}`. Dify supports deep object access, so you can extract nested values like `{{api_response.data.items[0].id}}` from previous HTTP responses.

### Timeout Configuration

HTTP requests have configurable timeouts to prevent hanging:
- **Connect timeout**: Maximum time to establish connection (default varies by deployment)
- **Read timeout**: Maximum time to read response data
- **Write timeout**: Maximum time to send request data
Timeouts are enforced to maintain workflow performance and prevent resource exhaustion.

### Authentication

The node supports multiple authentication types:**No Auth** (`type: "no-auth"`) - No authentication headers added **API Key** (`type: "api-key"`) with three subtypes:
- **Basic** (`type: "basic"`) - Adds Basic Auth header with base64 encoding
- **Bearer** (`type: "bearer"`) - Adds `Authorization: Bearer <token>` header
- **Custom** (`type: "custom"`) - Adds custom header with specified name and value

### Request Body

Choose the appropriate body type based on your API requirements:
- **JSON** for structured data
- **Form Data** for traditional web forms
- **Binary** for file uploads
- **Raw Text** for custom content types

## File Detection

The HTTP Request node automatically detects file responses using sophisticated logic:
1. **Content-Disposition analysis** - Checks for `attachment` disposition or filename parameters
2. **MIME type evaluation** - Analyzes content types to distinguish text from binary
3. **Content sampling** - For ambiguous types, samples first 1024 bytes to detect text patterns
Text-based responses (JSON, XML, HTML, etc.) are treated as regular data, while binary content becomes file variables.

## File Operations

The HTTP Request node handles file uploads and downloads seamlessly:

![HTTP node file upload](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1f2e33cf7bed33096b5aee145006193d.png)

HTTP node file upload

File upload configuration example

**File Uploads** use the binary request body option. Select file variables from previous nodes to send files to external services for document storage, media processing, or backup.**File Downloads** are automatically handled when responses contain file content. Downloaded files become available as file variables for use in downstream nodes.Configure robust error handling for production workflows that depend on external services:

![HTTP retry settings](https://assets-docs.dify.ai/2024/12/2e7c6080c0875e31a074c2a9a4543797.png)

HTTP retry settings

HTTP retry configuration

**Retry Settings** automatically retry failed requests up to 10 times with configurable intervals (maximum 5000ms). This handles temporary network issues or service unavailability.

![HTTP error handling](https://assets-docs.dify.ai/2024/12/91daa86d9770390ab2a41d6d0b6ed1e7.png)

HTTP error handling

HTTP error handling options

**Error Handling** defines alternative workflow paths when HTTP requests fail, ensuring your workflow continues executing even when external APIs are unavailable.

## Response Processing

HTTP responses become structured variables in subsequent nodes with separate access to:
- **Response Body** - The main content returned by the API
- **Status Code** - HTTP status for conditional logic
- **Headers** - Response metadata as key-value pairs
- **Files** - Any file content returned by the API
- **Size Information** - Content size in bytes with readable formatting (KB/MB)

### SSL Verification

SSL certificate verification is configurable per node (`ssl_verify` parameter). This allows connections to internal services with self-signed certificates while maintaining security for external APIs.

![Customer Feedback Classification workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/090975269f8998f906c5636dde8d9540.png)

Customer Feedback Classification workflow

Dynamic API integration example workflow

[Previous](https://docs.dify.ai/en/use-dify/nodes/parameter-extractor)[List Operator](https://docs.dify.ai/en/use-dify/nodes/list-operator)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/list-operator)