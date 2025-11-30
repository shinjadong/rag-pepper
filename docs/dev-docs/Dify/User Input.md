---
title: "User Input"
source: "https://docs.dify.ai/en/use-dify/nodes/user-input"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Entry point for workflow and chatflow applications"
tags:
  - "clippings"
---
## Introduction

The User Input node is a type of Start node where you can define what information to collect from end users when they run your application.Applications that start with this node run *on demand*, initiated by direct user interaction or API calls. You can also publish these applications as standalone web apps or MCP servers, expose them through backend service APIs, or use them as tools in other Dify applications.

Each application canvas can contain only one User Input node.

## Input Variable

### Preset

Preset input variables are system-defined and available by default.
- `userinput.files`: Files uploaded by end users when they run the application.
	For workflow applications, this preset variable has been considered *legacy* and maintained only for backward compatibility.We recommend using a [custom file input field](https://docs.dify.ai/en/use-dify/nodes/#file-input) instead to collect user files.
- `userinput.query` (for chatflows only): The text message automatically captured from the user’s latest chat turn.

### Custom

You can configure custom input fields in a User Input node to collect information from end users. Each field becomes a variable that can be referenced by downstream nodes. For example, if you add an input field with the variable name `user_name`, you can reference it as `{{user_name}}` throughout the workflow.There are seven types of input fields you can choose from to handle different kinds of user input.

The **Label Name** is displayed to your end users.

In a chatflow application, you can **Hide** any input variable to make it invisible to the end user while keeping it available for reference within the chatflow.

#### Text Input

- Short Text
- Paragraph

The short-text field accepts up to 256 characters. Use it for names, email addresses, titles, or any brief text input that fits on a single line.

#### Structured Input

#### File Input

- Single File
- File List

The single-file field allows users to upload one file of any supported type, either from their device or via a file URL. The uploaded file is available as a variable containing file metadata (name, size, type, etc.).

**File Processing** Files uploaded through a User Input node must be processed appropriately by subsequent nodes. The User Input node only collects files; it does not read or parse their content.Therefore, you need to connect specific nodes to extract and process the file content. For example:
- Document files can be routed to a Doc Extractor node for text extraction so that LLMs can understand their content.
- Images can be sent to LLM nodes with vision capabilities or specialized image processing tool nodes.
- Structured data files such as CSV or JSON can be processed with Code nodes to parse and transform the data.

When users upload multiple files with mixed types (e.g., images and documents), you can use a List Operator node to separate them by file type before routing them to appropriate processing branches.

## What’s Next

After setting up a User Input node, you can connect it to other nodes to process the collected data. Common patterns include:
- Send the input to an LLM node for processing.
- Use a Knowledge Retrieval node to find relevant information based on the input.
- Route the execution path to different branches with conditional logic based on the input.

[Previous](https://docs.dify.ai/en/use-dify/getting-started/key-concepts)[Overview](https://docs.dify.ai/en/use-dify/nodes/trigger/overview)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/trigger/overview)