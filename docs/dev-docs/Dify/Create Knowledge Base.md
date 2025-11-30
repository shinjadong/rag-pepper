---
title: "Create Knowledge Base"
source: "https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/introduction"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
Steps to upload documents to create a knowledge base:
1. Create a knowledge base and import either local document file or online data.
Import text data

Create a knowledge base and import either local document file or online data.

[View original](https://docs.dify.ai/en/use-dify/knowledge/import-content-data)
1. Choose a chunking mode and preview the spliting results. This stage involves content preprocessing and structuring, where long texts are divided into multiple smaller chunks.
Choose a chunk mode

Choose a chunking mode and preview the spliting results. This stage involves content preprocessing and structuring, where long texts are divided into multiple smaller chunks.

[View original](https://docs.dify.ai/en/use-dify/knowledge/chunking-and-cleaning-text)
1. Configure the indexing method and retrieval setting. Once the knowledge base receives a user query, it searches existing documents according to preset retrieval methods and extracts highly relevant content chunks.
Select the indexing method and retrieval setting

Configure the indexing method and retrieval setting. Once the knowledge base receives a user query, it searches existing documents according to preset retrieval methods and extracts highly relevant content chunks.

[View original](https://docs.dify.ai/en/use-dify/knowledge/setting-indexing-methods)
1. Wait for the chunk embeddings to complete.
2. Once finished, link the knowledge base to your application and start using it. You can then [integrate it into your application](https://docs.dify.ai/en/use-dify/knowledge/integrate-knowledge-within-application) to build an LLM that are capable of Q&A based on knowledge-bases. If you want to modify and manage the knowledge base further, take refer to [Knowledge Base and Document Maintenance](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/%5Bknowledge-and-documents-maintenance%5D\(/en/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents\)).
![](https://assets-docs.dify.ai/2024/12/a3362a1cd384cb2b539c9858de555518.png)

---

### Reference

#### ETL

In production-level applications of RAG, to achieve better data retrieval, multi-source data needs to be preprocessed and cleaned, i.e., ETL (extract, transform, load). To enhance the preprocessing capabilities of unstructured/semi-structured data, Dify supports optional ETL solutions: **Dify ETL** and [**Unstructured ETL**](https://unstructured.io/).

> Unstructured can efficiently extract and transform your data into clean data for subsequent steps.

ETL solution choices in different versions of Dify:
- The SaaS version defaults to using Unstructured ETL and cannot be changed;
- The community version defaults to using Dify ETL but can enable Unstructured ETL through [environment variables](https://docs.dify.ai/en/self-host/configuration/environments);
Differences in supported file formats for parsing:

Different ETL solutions may have differences in file extraction effects. For more information on Unstructured ETL’s data processing methods, please refer to the [official documentation](https://docs.unstructured.io/open-source/core-functionality/partitioning).

#### Embedding

**Embedding** transforms discrete variables (words, sentences, documents) into continuous vector representations, mapping high-dimensional data to lower-dimensional spaces. This technique preserves crucial semantic information while reducing dimensionality, enhancing content retrieval efficiency.**Embedding models**, specialized large language models, excel at converting text into dense numerical vectors, effectively capturing semantic nuances for improved data processing and analysis.For managing the knowledge base with metadata, see *[Metadata](https://docs.dify.ai/en/use-dify/knowledge/metadata)*.

[Previous](https://docs.dify.ai/en/use-dify/knowledge/readme)[1\. Import Text Data](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/import-text-data/readme)

[

Next

](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/import-text-data/readme)