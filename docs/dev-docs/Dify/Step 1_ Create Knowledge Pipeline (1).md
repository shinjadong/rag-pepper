---
title: "Step 1: Create Knowledge Pipeline"
source: "https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
![Create Knowledge Pipeline](https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-1.png?w=280&fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=a422d60b1eb853e48c387c4f285a6292)

Create Knowledge Pipeline

Navigate to Knowledge at the top, then click Create from Knowledge Pipeline on the left. There’re three ways for you to get started.

### Build from Scratch

![Build from Scratch](https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-2.png?w=280&fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=df06ae37818bf3d5d8be405387b5b759)

Build from Scratch

Click Blank Knowledge Pipeline to build a custom pipeline from scratch. Choose this option when you need custom processing strategies based on specific data source and business requirements.

### Templates

Dify offers two types of templates: **Built-in Pipeline** and **Customized**. Both template cards display name of knowledge base, description, and tags (including chunk structure).![](https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-4-1.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=eb94d19335b57c9fafc8e78bedeba375)

#### Built-in Pipeline

Built-in pipelines are official knowledge base templates pre-configured by Dify. These templates are optimized for common document structures and use cases. Simply click **Choose** to get started.![Built-in Templates](https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-4.png?w=280&fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=80648fee23066a8004547e1b562dc81e)

Built-in Templates

**Types**

| Name | Chunk Structure | Index Method | Retrieval Setting | Description |
| --- | --- | --- | --- | --- |
| General Mode-ECO | General | Economical | Inverted Index | Divide document content into smaller paragraphs, directly used for matching user queries and retrieval. |
| Parent-child-HQ | Parent-Child | High Quality | Hybrid Search | Adopt advanced chunking strategy, dividing document text into larger parent chunks and smaller child chunks. The parent chunks contain child chunks which ensure both retrieval precision and maintain contextual integrity. |
| Simple Q&A | Question & Answer | High Quality | Vector Search | Convert tabular data into question-answer format, using question matching to quickly hit corresponding answer information. |
| LLM Generated Q&A | Question & Answer | High Quality | Vector Search | Generate structured question-answer pairs with large language models based on original text paragraphs. Find relevant answer by using question matching mechanism. |
| Convert to Markdown | Parent-child | High Quality | Hybrid Search - Weighted Score | Designed for Office native file formats such as DOCX, XLSX, and PPTX, converting them to Markdown format for better information processing. ⚠️ Note: PDF files are not recommended. |

To preview the selected built-in pipeline, click **Details** on any template card. Then, check information in the popup window, including: orchestration structure, pipeline description, and chunk structure. Click **Use this Knowledge Pipeline** for orchestration.![Template Details](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/create-knowledge-pipeline-5.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=39d8fdbdd078cc7791c8653fff6306f9)

Template Details

#### Customized

![Customized Templates](https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-6.png?w=280&fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=5a605694bc1a60a11a8227743a9a111c)

Customized Templates

Customized templates are user-created and published knowledge pipeline. You can choose a template to start, export the DSL, or view detailed information for any template.![Template Actions](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/create-knowledge-pipeline-7.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=ba5685e2f98d1c5847d05bbeda99d623)

Template Actions

To create a knowledge base from a template, click **Choose** on the template card. You can also create knowledge base by clicking **Use this Knowledge Pipeline** when previewing a template. Click **More** to edit pipeline information, export pipeline, or delete the template.

### Import Pipeline

![Import DSL](https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-3.png?w=280&fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=84358c8af4d34409ccae8271ae5aef0e)

Import DSL

Import a pipeline of a previously exported knowledge pipeline to quickly reuse existing configurations and modify them for different scenarios or requirements. Navigate to the bottom left of the page and click **Import from a DSL File**. Dify DSL is a YAML-based standard that defines AI application configurations, including model parameters, prompt design, and workflow orchestration. Similar to workflow DSL, knowledge pipeline uses the same YAML format standard to define processing workflows and configurations within a knowledge base.What’s in a knowledge pipeline DSL:

[Previous](https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/readme)[Step 2: Knowledge Pipeline Orchestration](https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/knowledge-pipeline-orchestration)

[

Next

](https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/knowledge-pipeline-orchestration)