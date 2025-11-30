---
title: "Parameter Extractor"
source: "https://docs.dify.ai/en/use-dify/nodes/parameter-extractor"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Convert natural language to structured data using LLM intelligence"
tags:
  - "clippings"
---
The Parameter Extractor node converts unstructured text into structured data using LLM intelligence. It bridges the gap between natural language input and the structured parameters that tools, APIs, and other workflow nodes require.

## Configuration

### Input and Model Selection

Select the **Input Variable** containing the text you want to extract parameters from. This typically comes from user input, LLM responses, or other workflow nodes.Choose a **Model** with strong structured output capabilities. The Parameter Extractor relies on the LLM’s ability to understand context and generate structured JSON responses.

### Parameter Definition

Define the parameters you want to extract by specifying:
- **Parameter Name** - The key that will appear in the output JSON
- **Data Type** - String, number, boolean, array, or object
- **Description** - Helps the LLM understand what to extract
- **Required Status** - Whether the parameter must be present
You can manually define parameters or **quickly import from existing tools** to match the parameter requirements of downstream nodes.

### Extraction Instructions

Write clear instructions describing what information to extract and how to format it. Providing examples in your instructions improves extraction accuracy and consistency for complex parameters.

![Arxiv Paper Retrieval Tool](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/a8bae4106a015c76ebb0a165f2409458.png)

Arxiv Paper Retrieval Tool

Parameter extraction for Arxiv paper retrieval

## Advanced Configuration

### Inference Mode

Choose between two extraction approaches based on your model’s capabilities:**Function Call/Tool Call** uses the model’s structured output features for reliable parameter extraction with strong type compliance.**Prompt-based** relies on pure prompting for models that may not support function calling or when prompt-based extraction performs better.

### Memory

Enable memory to include conversation history when extracting parameters. This helps the LLM understand context in interactive dialogues and improves extraction accuracy for conversational workflows.

## Output Variables

The node provides both extracted parameters and built-in status variables:**Extracted Parameters** appear as individual variables matching your parameter definitions, ready for use in downstream nodes.**Built-in Variables** include status information:
- `__is_success` - Extraction success status (1 for success, 0 for failure)
- `__reason` - Error description when extraction fails

![Data format conversion workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/71d8e48d842342668f92e6dd84fc03c1.png)

Data format conversion workflow

Data format conversion example

[Previous](https://docs.dify.ai/en/use-dify/nodes/variable-assigner)[HTTP Request](https://docs.dify.ai/en/use-dify/nodes/http-request)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/http-request)