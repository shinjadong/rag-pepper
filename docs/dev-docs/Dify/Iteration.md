---
title: "Iteration"
source: "https://docs.dify.ai/en/use-dify/nodes/iteration"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Process arrays by applying workflows to each element"
tags:
  - "clippings"
---
The Iteration node processes arrays by running the same workflow steps on each element sequentially or in parallel. Use it for batch processing tasks that would otherwise hit limits or be inefficient as single operations.

![Iteration node overview](https://assets-docs.dify.ai/2025/04/5f3f124c16b9e3565853f125f7db0e32.png)

Iteration node overview

Iteration node processing workflow

## How Iteration Works

The node takes an array input and creates a sub-workflow that runs once for each array element. During each iteration, the current item and its index are available as variables that internal nodes can reference.**Core Components:**
- **Input Variables** - Array data from upstream nodes
- **Internal Workflow** - The processing steps to perform on each element
- **Output Variables** - Collected results from all iterations (also an array)

## Configuration

### Array Input

Connect an array variable from upstream nodes such as Parameter Extractor, Code nodes, Knowledge Retrieval, or HTTP Request responses.

### Built-in Variables

Each iteration provides access to:
- `items[object]` - The current array element being processed
- `index[number]` - The current iteration index (starting from 0)

### Processing Mode

- Sequential Mode
- Parallel Mode

**Sequential Processing** - Items processed one after another in order **Streaming Support** - Results can be output progressively using Answer nodes **Resource Management** - Lower memory usage, predictable execution order **Best For** - When order matters or when using streaming output

![Processing mode comparison](https://assets-docs.dify.ai/2024/12/2656dec26d6357556a280fcd69ccd9a7.png)

Processing mode comparison

Sequential vs parallel processing comparison

![Parallel mode setting](https://assets-docs.dify.ai/2024/12/516af5e7427fce9a58fa9d9b583230d4.png)

Parallel mode setting

Enable parallel mode in iteration settings

Configure how to handle processing failures for individual array elements:**Terminate** - Stop processing when any error occurs and return the error message **Continue on Error** - Skip failed items and continue processing, outputting null for failed elements **Remove Failed Results** - Skip failed items and return only successful results Input-output correspondence examples:
- Input: `[1, 2, 3]`
- Output with Continue on Error: `[result-1, null, result-3]`
- Output with Remove Failed: `[result-1, result-3]`

## Long Article Generation Example

Generate lengthy content by processing chapter outlines individually:

![Long story generator](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3a403551d48b178d0a41ce2a5748dd2d.png)

Long story generator

Long article generation workflow

**Workflow Steps:**
1. **Start Node** - User provides story title and outline
2. **LLM Node** - Generate detailed chapter breakdown
3. **Parameter Extractor** - Convert chapter list to structured array
4. **Iteration Node** - Process each chapter with internal LLM
5. **Answer Node** - Stream chapter content as it’s generated

![Start node setup](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3af1c2ed0df00f19e584bcf511302f55.png)

Start node setup

Start node configuration for story input

![Parameter extraction setup](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d3beee536ff3c35f4e1eb1ab610f35d7.png)

Parameter extraction setup

Parameter extraction for chapter structure

![Iteration node configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/ac91582998868004b298afe2f04e5589.png)

Iteration node configuration

Iteration configuration with LLM processing

Parameter extraction effectiveness depends on model capabilities and instruction quality. Use stronger models and provide examples in instructions to improve results.

## Output Processing

Iteration nodes output arrays that often need conversion for final use:

### Convert Array to Text

- Using Code Node
- Using Template Node

```
def main(articleSections: list):

    return {

        "result": "\n".join(articleSections)

    }
```

![Code node conversion](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8be2372b00a802e981efe6f0ceff815b.png)

Code node conversion

Code node array conversion

[Previous](https://docs.dify.ai/en/use-dify/nodes/ifelse)[Loop](https://docs.dify.ai/en/use-dify/nodes/loop)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/loop)