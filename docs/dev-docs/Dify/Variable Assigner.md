---
title: "Variable Assigner"
source: "https://docs.dify.ai/en/use-dify/nodes/variable-assigner"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Manage persistent conversation variables in chatflow applications"
tags:
  - "clippings"
---
The Variable Assigner node manages persistent data in chatflow applications by writing to conversation variables (Understand the different types of variables [here](https://docs.dify.ai/en/use-dify/nodes/en/use-dify/getting-started/key-concepts#variables)). Unlike regular workflow variables that reset with each execution, conversation variables persist throughout an entire chat session.

![Variable Assigner interface](https://assets-docs.dify.ai/2024/11/83d0b9ef4c1fad947b124398d472d656.png)

Variable Assigner interface

Variable Assigner node configuration

## Conversation Variables vs Workflow Variables

**Workflow Variables** exist only during a single workflow execution and reset when the workflow completes.**Conversation Variables** persist across multiple conversation turns within the same chat session, enabling stateful interactions and contextual memory.This persistence enables contextual conversations, user personalization, stateful workflows, and progress tracking across multiple user interactions.

## Configuration

Configure which conversation variables to update and specify their source data. You can assign multiple variables in a single node.

![Variable assignment configuration](https://assets-docs.dify.ai/2024/11/ee15dee864107ba5a93b459ebdfc32cf.png)

Variable assignment configuration

Variable assignment configuration interface

**Variable** - Select the conversation variable to write to **Set Variable** - Choose the source data from upstream workflow nodes **Operation Mode** - Determine how to update the variable (overwrite, append, clear, etc.)

## Operation Modes

Different variable types support different operations based on their data structure:

- String Variables
- Number Variables
- Object Variables
- Array Variables

**Overwrite** - Replace the entire string value with new content **Clear** - Empty the variable, setting it to null or blank **Set** - Manually type in a fixed value

Array operations are particularly powerful for building memory systems, checklists, and conversation histories that grow over time.

## Common Implementation Patterns

### Smart Memory System

Build chatbots that automatically detect and store important information from conversations:

![Smart memory implementation](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8d0492814b1515f50e87b2900ff400db.png)

Smart memory implementation

Smart memory system workflow

The system analyzes user input for memorable facts, extracts structured information, and appends it to a persistent memories array for future reference in conversations.

### User Preferences Storage

Store user preferences like language settings, notification preferences, or display options:

![User preferences workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1867d608a7d009431b73377ed65b427b.png)

User preferences workflow

User preferences management

Use **Overwrite** mode to capture initial preferences from user input, then reference them in all subsequent LLM responses for personalized interactions.

### Progressive Checklists

Build guided workflows that track completion status across multiple conversation turns:

![Progressive checklist workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/c4362b01298b12e7d6fcd9e798f3165a.png)

Progressive checklist workflow

Progressive checklist implementation

Use array conversation variables to track completed items. The Variable Assigner updates the checklist each turn, while the LLM references it to guide users through remaining tasks.

[Previous](https://docs.dify.ai/en/use-dify/nodes/doc-extractor)[Parameter Extractor](https://docs.dify.ai/en/use-dify/nodes/parameter-extractor)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/parameter-extractor)