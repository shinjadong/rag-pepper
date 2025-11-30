---
title: "Step 2: Knowledge Pipeline Orchestration"
source: "https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/knowledge-pipeline-orchestration"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
Imagine setting up a factory production line where each station (node) performs a specific task, and you connect them to assemble widgets into a final product. This is knowledge pipeline orchestration—a visual workflow builder that allows you to configure data processing sequences through a drag-and-drop interface. It provides control over document ingestion, processing, chunking, indexing, and retrieval strategies.In this section, you’ll learn about the knowledge pipeline process, understand different nodes, how to configure them, and customize your own data processing workflows to efficiently manage and optimize your knowledge base.

### Interface Status

When entering the knowledge pipeline orchestration canvas, you’ll see:
- **Tab Status**: Documents, Retrieval Test, and Settings tabs will be grayed out and unavailable at the moment
- **Essential Steps**: You must complete knowledge pipeline orchestration and publishing before uploading files
Your starting point depends on the template choice you made previously. If you chose **Blank Knowledge Pipeline**, you’ll see a canvas that contains Knowledge Base node only. There’ll be a note with guide next to the node that walks you through the general steps of pipeline creation.![Blank Pipeline](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/create-knowledge-pipeline-8.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=dba9966ff2a8c3e51a22fc4a9a38c122)

Blank Pipeline

If you selected a specific pipeline template, there’ll be a ready-to-use workflow that you can use or modify on the canvas right away.![Template Pipeline](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/create-knowledge-pipeline-9.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=3bfdb01b50d5bd9f85b53dcf370142ce)

Template Pipeline

## The Complete Knowledge Pipeline Process

Before we get started, let’s break down the knowledge pipeline process to understand how your documents are transformed into a searchable knowledge base.The knowledge pipeline includes these key steps:

Data Source → Data Processing (Extractor + Chunker) → Knowledge Base Node (Chunk Structure + Retrieval Setting) → User Input Field → Test & Publish

1. **Data Source**: Content from various data sources (local files, Notion, web pages, etc.)
2. **Data Processing**: Process and transform data content
	- Extractor: Parse and structure document content
	- Chunker: Split structured content into manageable segments
3. **Knowledge Base**: Set up chunk structure and retrieval settings
4. **User Input Field**: Define parameters that pipeline users need to input for data processing
5. **Test & Publish**: Validate and officially activate the knowledge base

---

## Step 1: Data Source

In a knowledge base, you can choose single or multiple data sources. Currently, Dify supports 4 types of data sources: **file upload, online drive, online documents, and web crawler**.Visit the [Dify Marketplace](https://marketplace.dify.ai/) for more data sources.

### File Upload

Upload local files through drag-and-drop or file selection.![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-1.PNG?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=3cf88cfdf65edb4cc9b496c187780e33)

**Configuration Options** **Limitations** **Output Variables**

---

### Online Document

#### Notion

Integrate with your Notion workspace to seamlessly import pages and databases, always keeping your knowledge base automatically updated.![Notion](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-2.PNG?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=3fe8dd70bef6d58a8751785eae260c1e)

**Configuration Options**

---

### Web Crawler

Transform web content into formats that can be easily read by large language models. The knowledge base supports Jina Reader and Firecrawl.

#### Jina Reader

An open-source web parsing tool providing simple and easy-to-use API services, suitable for fast crawling and processing web content.

![Jina Reader](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-3.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=965a2b443f2c79d933a116723af33273)

Jina Reader

**Parameter Configuration**

#### Firecrawl

An open-source web parsing tool that provides more refined crawling control options and API services. It supports deep crawling of complex website structures, recommended for batch processing and precise control.![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-4.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=398423f8e068968f2fc848673d14fdcb)

**Parameter Configuration**

---

### Online Drive

Connect your online cloud storage services (e.g., Google Drive, Dropbox, OneDrive) and let Dify automatically retrieve your files. Simply select and import the documents you need for processing, without manually downloading and re-uploading files.

Need help with authorization? Please check for detailed guidance on authorizing different data sources.

---

## Step 2: Set Up Data Processing Tools

In this stage, these tools extract, chunk, and transform the content for optimal knowledge base storage and retrieval. Think of this step like meal preparation. We clean raw materials up, chop them into bite-sized pieces, and organize everything, so the dish can be cooked up quickly when someone orders it.

### Doc Processor

Documents come in different formats - PDF, XLSX, DOCX. However, LLM can’t read these files directly. That’s where extractors come in. They support multiple formats and handle the conversion, so your content is ready for the next step of the LLMs.You can choose Dify’s Doc Extractor to process files, or select tools based on your needs from Marketplace which offers Dify Extractor and third-party tools such as Unstructured.

#### Doc Extractor

![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-4-1.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=730bf3fa7d78750a4e663fea9e4f7386) As an information processing center, document extractor node identifies and reads files from input variables, extracts information, and finally converts them into a format that works with the next node.

For more information, please refer to the [Document Extractor](https://docs.dify.ai/en/use-dify/nodes/doc-extractor).

#### Dify Extractor

Dify Extractor is a built-in document parser presented by Dify. It supports multiple common file formats and is specially optimized for Doc files. It can extract and store images from documents and return image URLs.![Dify Extractor](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-5.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=7a9004471c0ddeee518a3eb7d33e0e22)

Dify Extractor

#### Unstructured

Explore more tools in the [Dify Marketplace](https://marketplace.dify.ai/).

---

### Chunker

Similar to human limited attention span, large language models cannot process huge amount of information simultaneously. Therefore, after information extraction, the chunker splits large document content into smaller and manageable segments (called “chunks”).Different documents require different chunking strategies. A product manual works best when split by product features, while research papers should be divided by logical sections. Dify offers 3 types of chunkers for various document types and use cases.

#### Overview of Different Chunkers

#### Common Text Pre-processing Rules

All chunkers support these text cleaning options:

#### General Chunker

Basic document chunking processing, suitable for documents with relatively simple structures. You can configure text chunking and text preprocessing rules according to the following configuration.**Input and Output Variable** **Chunk Settings**

#### Parent-child Chunker

By using a dual-layer segmentation structure to resolve the contradiction between context and accuracy, parent-child clunker achieves the balance between precise matching and comprehensive contextual information in Retrieval Augmented Generation (RAG) systems.**How Parent-child Chunker Works** Child Chunks for query matching: Small, precise information segments (usually single sentences) to match user queries with high accuracy.Parent Chunks provide rich context: Larger content blocks (paragraphs, sections, or entire documents) that contain the matching child chunks, giving the large language model (LLM) comprehensive background information.**Chunk Settings**

#### Q&A Processor

Combining extraction and chunking in one node, Q&A Processor is specifically designed for structured Q&A datasets from CSV and Excel files. Perfect for FAQ lists, shift schedules, and any spreadsheet data with clear question-answer pairs.**Input and Output Variable** **Variable Configuration**

---

## Step 3: Configure Knowledge Base Node

Now that your documents are processed and chunked, it’s time to set up how they’ll be stored and retrieved. Here, you can select different indexing methods and retrieval strategies based on your specific needs.Knowledge base node configuration includes: Input Variable, Chunk Structure, Index Method, and Retrieval Settings.

### Chunk Structure

![Chunk Structure](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-8.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=cd6a0356fdf6eecc235aaf3e74a71927)

Chunk Structure

Chunk structure determines how the knowledge base organizes and indexes your document content. Choose the structure mode that best fits your document type, use case, and cost.The knowledge base supports three chunk modes: **General Mode, Parent-child Mode, and Q&A Mode**. If you’re creating a knowledge base for the first time, we recommend choosing Parent-child Mode.

**Important Reminder**: Chunk structure cannot be modified once saved and published. Please choose carefully.

#### General Mode

Suitable for most standard document processing scenarios. It provides flexible indexing options—you can choose appropriate indexing methods based on different quality and cost requirements.General mode supports both high-quality and economical indexing methods, as well as various retrieval settings.

#### Parent-child Mode

It provides precise matching and corresponding contextual information during retrieval, suitable for professional documents that need to maintain complete context.Parent-child mode supports HQ (High Quality) mode only, offering child chunks for query matching and parent chunks for contextual information during retrieval.

#### Q&A Mode

Create documents that pair questions with answers when using structured question-answer data. These documents are indexed based on the question portion, enabling the system to retrieve relevant answers based on query similarity.Q&A Mode supports HQ (High Quality) mode only.

### Input Variable

Input variables receive processing results from data processing nodes as the data source for knowledge base. You need to connect the output from chunker to the knowledge base as input.The node supports different types of standard inputs based on the selected chunk structure:
- **General Mode**: x Array\[Chunk\] - General chunk array
- **Parent-child Mode**: x Array\[ParentChunk\] - Parent chunk array
- **Q&A Mode**: x Array\[QAChunk\] - Q&A chunk array

### Index Method & Retrieval Setting

The index method determines how your knowledge base builds content indexes, while retrieval settings provide corresponding retrieval strategies based on the selected index method. Think of it in this way: index method determines how to organize your documents, while retrieval settings tell users what methods they can use to find documents.The knowledge base provides two index methods: **High Quality** and **Economy**, each offering different retrieval setting options.High quality mode uses embedding models to convert segmented text blocks into numerical vectors, helping to compress and store large amounts of text information more effectively. This enables the system to find semantically relevant accurate answers even when the user’s question wording doesn’t exactly match the document.In economy mode, each block uses 10 keywords for retrieval without calling embedding models, generating no costs.

Please refer to [Select the Indexing Method and Retrieval Setting](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/setting-indexing-methods) for more details.

#### Index Methods and Retrieval Settings

You can also refer to the table below for information on configuring chunk structure, indexing methods, parameters, and retrieval settings.

---

## Step 4: Create User Input Form

User input forms are essential for collecting the initial information your pipeline needs to run effectively. Similar to [start node](https://docs.dify.ai/en/use-dify/nodes/start) in workflow, this form gathers necessary details from users - such as files to upload, specific parameters for document processing - ensuring your pipeline has all the information it needs to deliver accurate results.This way, you can create specialized input forms for different use scenarios, improving pipeline flexibility and usability for various data sources or document processing steps.

### Create User Input Form

There’re two ways to create user input field:
1. **Pipeline Orchestration Interface**  
	Click on the **Input field** to start creating and configuring input forms.\\ ![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-9.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=98ed68b0f89e283381d80e767c1ba570)
2. **Node Parameter Panel**  
	Select a node. Then, in parameter input on the right-side panel, click + Create user input for new input items. New input items will also be collected in the Input Field. ![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-10.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=641daa36a3cf66f98afcd989fd602512)

### Add User Input Fields

#### Unique Inputs for Each Entrance

![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-11.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=503ff9f3674f1c7f5d706c14d4c8bfdc) These inputs are specific to each data source and its downstream nodes. Users only need to fill out these fields when selecting the corresponding data source, such as different URLs for different data sources.![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-12.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=df74440ce812d1dee424191026307f22)

How to create

#### Global Inputs for All Entrances

![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-13.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=ea8ca2414564dd8e629108bfb053194b) Global shared inputs can be referenced by all nodes. These inputs are suitable for universal processing parameters, such as delimiters, maximum chunk length, document processing configurations, etc. Users need to fill out these fields regardless of which data source they choose.**How to create**: Click the `+` button on the right side of Global Inputs to add fields that can be referenced by any node.

### Supported Input Field Types

The knowledge pipeline supports seven types of input variables:![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-14.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=6035e9852afa8a899753b75b29d1e988)

For more information about supported field types, please refer to the [Input Fields documentation](https://docs.dify.ai/en/use-dify/nodes/start#input-field).

### Field Configuration Options

All input field types include: required, optional, and additional settings. You can set whether fields are required by checking the appropriate option.After completing configuration, click the preview button in the upper right corner to browse the form preview interface. You can drag and adjust field groupings. If an exclamation mark appears, it indicates that the reference is invalid after moving.![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-15.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=18b9dec017c99ef2b840b67ae89e2db9)

---

## Step 5: Name the Knowledge Base

![Name Knowledge Base](https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-11.png?w=280&fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=fa3147fb13b420acf24f2d269fde965b)

Name Knowledge Base

By default, the knowledge base name will be “Untitled + number”, permissions are set to “Only me”, and the icon will be an orange book. If you import it from a DSL file, it will use the saved icon.Edit knowledge base inforamtion by clicking **Settings** in the left panel and fill in the information below:
- **Name & Icon**  
	Pick a name for your knowledge base.  
	Choose an emoji, upload an image, or paste an image URL as the icon of this knowledge base.
- **Knowledge Description** Provide a brief description of your knowledge base. This helps the AI better understand and retrieve your data. If left empty, Dify will apply the default retrieval strategy.
- **Permissions**  
	Select the appropriate access permissions from the dropdown menu.

---

## Step 6: Testing

You’re almost there! This is the final step of the knowledge pipeline orchestration.After completing the orchestration, you need to validate all the configuration first. Then, do some running tests and confirm all the settings. Finally, publish the knowledge pipeline.

### Configuration Completeness Check

Before testing, it’s recommended to check the completeness of your configuration to avoid test failures due to missing configurations.Click the checklist button in the upper right corner, and the system will display any missing parts.![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-16.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=9d1f9c1b5923e6af2c4acc12899c5320) After completing all configurations, you can preview the knowledge base pipeline’s operation through test runs, confirm that all settings are accurate, and then proceed with publishing.

### Test Run

![](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-17.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=04ac4d5c9fa83858b7c069c322909a3c)
1. **Start Test**: Click the “Test Run” button in the upper right corner
2. **Import Test File**: Import files in the data source window that pops up on the right

**Important Note**: For better debugging and observation, only one file upload is allowed per test run.

1. **Fill Parameters**: After successful import, fill in corresponding parameters according to the user input form you configured earlier
2. **Start Test Run**: Click next step to start testing the entire pipeline
During testing, you can access [History Logs](https://docs.dify.ai/en/use-dify/monitor/logs) (track all run records with timestamps, execution status, and input/output summaries) and [Variable Inspector](https://docs.dify.ai/en/use-dify/debug/variable-inspect) (a dashboard at the bottom showing input/output data for each node to help identify issues and verify data flow) for efficient troubleshooting and error fixing.![Testing Tools](https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/knowledge-pipeline-orchestration-18.png?w=280&fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=23e31974b45fbef55615f61bda10ff1b)

Testing Tools

[Previous](https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline)[Step 3: Publish Knowledge Pipeline](https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/publish-knowledge-pipeline)

[

Next

](https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/publish-knowledge-pipeline)