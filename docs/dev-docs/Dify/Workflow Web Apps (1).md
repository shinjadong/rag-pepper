---
title: "Workflow Web Apps"
source: "https://docs.dify.ai/en/use-dify/publish/webapp/workflow-webapp"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Turn your workflows into powerful web applications with batch processing, result management, and streamlined user experiences"
tags:
  - "clippings"
---
Workflow web apps transform your Dify workflows into production-ready applications that handle everything from single runs to large-scale batch operations. Users get a clean interface for input, real-time processing feedback, and comprehensive result management.

## How Workflow Apps Work

When you publish a workflow, Dify automatically creates a web interface that:
- **Collects input parameters** through forms based on your workflow’s start variables
- **Processes requests** using your complete workflow logic
- **Handles results** with built-in saving, copying, and management features
- **Scales automatically** from single runs to batch processing hundreds of items

Unlike chat apps that maintain conversation context, workflow apps are designed for discrete tasks that produce specific outputs.

## Single Execution

The default mode for workflow apps handles individual requests with real-time processing:

![Single workflow execution interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/4c5380cf71066d933082f7c30deacb01.png)

Single workflow execution interface

**User Experience:**
1. **Fill input form** - Users provide parameters based on your workflow’s start variables
2. **Click run** - The workflow executes with real-time progress indication
3. **View results** - Output appears with immediate access to copy, save, and feedback options
4. **Take actions** - Users can save important results, provide feedback, or generate similar outputs
Each result includes built-in actions:
- **Copy** - One-click copying to clipboard for easy sharing
- **Save** - Store results in the app’s saved items for later access
- **Feedback** - Like/dislike ratings to help improve your workflow
- **More like this** - Generate variations based on the current result (if enabled)

## Batch Processing

When you need to run the same workflow on multiple inputs, batch processing handles hundreds of executions simultaneously:

Perfect for tasks like generating content for multiple topics, processing customer data, or analyzing large datasets.

### Setting Up Batch Runs

### Batch Processing Benefits

- **Parallel execution** - Multiple workflow runs happen simultaneously
- **Progress tracking** - Real-time updates on completion status
- **Bulk export** - Download all results as a CSV file when finished
- **Error handling** - Failed items are clearly marked with error details

CSV files must use Unicode encoding to prevent import failures. When saving from Excel or similar tools, explicitly select “Unicode (UTF-8)” encoding.

## Result Management

Workflow apps include comprehensive result management to help users organize and reuse outputs:

### Saving Results

![Saved results interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/3cdd15e87aa1f1aae9f6abadb0f16d1f.png)

Saved results interface

**How saving works:**
- Users click “Save” on any result they want to keep
- Saved items appear in the dedicated “Saved” tab
- Each saved result includes the original inputs and full outputs
- Users can organize saved results and access them anytime

Saved results persist across user sessions, making workflow apps useful for building personal libraries of outputs.

### Generating Variations

When you enable “More like this” in your workflow settings, users can generate variations of successful results:

![More like this feature](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/65fb111d8e89a8f7b761859265e42f0a.png)

More like this feature

**How it works:**
1. User gets a result they like
2. They click “More like this” to generate similar outputs
3. The workflow runs again with slight variations to produce different but related results
4. Users can iterate until they find the perfect output

[Previous](https://docs.dify.ai/en/use-dify/publish/README)[Chat Web Apps](https://docs.dify.ai/en/use-dify/publish/webapp/chatflow-webapp)

[

Next

](https://docs.dify.ai/en/use-dify/publish/webapp/chatflow-webapp)