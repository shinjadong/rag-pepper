---
title: "Tools"
source: "https://docs.dify.ai/en/use-dify/nodes/tools"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Connect to external services and APIs with pre-built integrations"
tags:
  - "clippings"
---
The Tools node connects your workflow to external services and APIs through pre-built integrations. Unlike HTTP Request nodes, Tools provide structured interfaces, built-in error handling, and simplified configuration for popular services.

![Tools node interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/0f0255764a3f459f0b3c708db1cb32c9.png)

Tools node interface

Tools node configuration interface

## Tool Types

Dify supports multiple types of tools to handle different integration needs:

![Tool categories](https://assets-docs.dify.ai/2025/04/f37cce4ccbb7456154cfa9eacda6b322.png)

Tool categories

Available tool categories and options

## Configuration

### Authentication

Many tools require API keys or OAuth authentication. Configure these credentials in the **Tools** section of your workspace before using them in workflows. Authentication is handled automatically once configured.

### Input Parameters

Tools provide structured forms with validation for input configuration. Set parameters using variables from previous workflow nodes. The interface automatically handles data type validation and provides helpful descriptions for each parameter.

### Output Handling

Tools return structured data that becomes available as variables for downstream nodes. Output schemas are predefined, ensuring compatibility and reducing integration complexity.

## Advantages Over HTTP Requests

**Structured Interfaces** provide form-based configuration with built-in validation, making setup easier than manual HTTP request configuration.**Built-in Error Handling** includes automatic retry logic and error management, reducing the complexity of handling API failures.**Type Safety** ensures input and output schemas maintain data compatibility between workflow nodes.**Documentation** includes usage examples and detailed parameter descriptions for each tool.Configure robust error handling for tools that depend on external services:

![Tool retry settings](https://assets-docs.dify.ai/2024/12/34867b2d910d74d2671cd40287200480.png)

Tool retry settings

Tool retry configuration

**Retry Settings** automatically retry failed tool executions up to 10 times with configurable intervals (maximum 5000ms). This handles temporary service issues or network problems.

![Tool error handling](https://assets-docs.dify.ai/2024/12/39dc3b5881d9a5fe35b877971f70d3a6.png)

Tool error handling

Tool error handling options

**Error Handling** defines alternative workflow paths when tool execution fails, ensuring your workflow continues even when external services are unavailable.

## Creating Custom Tools

**OpenAPI Integration** allows you to import any service with an OpenAPI/Swagger specification. Once imported, the service becomes available as a tool with the same ease of use as built-in options.**Workflow Publishing** converts multi-node workflows into single-node tools that can be reused across different applications. This promotes modularity and simplifies complex workflow management.

## Tool Management

Access tool configuration through **Tools** in your workspace navigation. Here you can manage authentication credentials, import custom tools, configure MCP servers, and publish workflows as tools.For detailed guidance on tool creation, management, and publishing workflows as tools, see the [Tool Configuration Guide](https://docs.dify.ai/plugin-dev-en/getting-started-dify-plugin).

[Previous](https://docs.dify.ai/en/use-dify/nodes/agent)[Question Classifier](https://docs.dify.ai/en/use-dify/nodes/question-classifier)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/question-classifier)