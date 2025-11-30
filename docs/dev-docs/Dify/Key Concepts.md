---
title: "Key Concepts"
source: "https://docs.dify.ai/en/use-dify/getting-started/key-concepts"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Quick overview of essential Dify concepts"
tags:
  - "clippings"
---
### Dify App

Dify is made for agentic app building. In **Studio**, you can quickly build agentic workflows via a drag & drop interface and publish them as apps. You can access published apps via API, the web, or as an [MCP server](https://docs.dify.ai/en/use-dify/publish/publish-mcp). Dify offers two main app types: workflow and chatflow. You will need to choose an app type when creating a new app.

We recommend choosing Workflow or Chatflow your app type. But in addition to these, Dify also offers 3 more basic app types: Chatbot, Agent, and Text Generator.![22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png](https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=b1fa00713a5beb1fa1ae9601e31d8a29 "22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png") These app types run on the same workflow engine underneath, but comes with simpler legacy interfaces:![chatbot-interface.png](https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/chatbot-interface.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=342873c2954ac135b1b5737828b99eab "chatbot-interface.png")

### Workflow

Build workflow apps to handle single-turn tasks. The webapp interface and API provides easy access to batch execute many tasks at once.

Underneath it all, workflow forms the basis for all other app types in Dify.

You can specify how and when to start your workflow. There are two types of Start nodes:
- **[User Input](https://docs.dify.ai/en/use-dify/nodes/user-input)**: Direct user interaction or API call invokes the app.
- **[Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/overview)**: The application runs automatically on a schedule or in response to a specific third-party event.
User Input and Trigger Start nodes are mutually exclusive—they cannot be used on the same canvas. To switch between them, right-click the current start node > **Change Node**. Alternatively, delete the current start node and add a new one.

Only workflows started by User Input can be published as standalone web apps or MCP servers, exposed through backend service APIs, or used as tools in other Dify applications.

### Chatflow

Chatflow is a special type of workflow app that gets triggered at every turn of a conversation. Other than workflow features, chatflow comes with the ability to store and update custom conversation-specific variables, enable memory in LLM nodes, and stream formatted text, images, and files at different points throughout the chatflow run.Unlike workflow, chatflow can’t use [Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/overview) to start.

### Dify DSL

All Dify apps can be exported into a YAML file in Dify’s own DSL (Domain-Specific Language) and you may create Dify apps from these DSL files directly. This makes it easy to port apps to other Dify instances and share with others.

### Variables

A variable is a labeled container to store information, so you can find and use that information later by referencing its name. You’ll come across different types of variables when building a Dify app:**Inputs**: You can specify any number of input variables at the [User Input](https://docs.dify.ai/en/use-dify/nodes/user-input) node for your app’s end users to fill in.![CleanShot 2025-08-04 at 14.34.04@2x.png](https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/CleanShot2025-08-04at14.34.04@2x.png?w=280&fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=cf26c4576ccfa850cc091e26272a32fc)

CleanShot 2025-08-04 at 14.34.04@2x.png

Additionally, the User Input node comes with a set of input variables that you can reference later in the flow. Depending on the app type (workflow or chatflow), different variables are provided.

- Workflow
- Chatflow

| Variable Name | Data Type | Description | Notes |
| --- | --- | --- | --- |
| `sys.user_id` | String | User ID: A unique identifier automatically assigned by the system to each user when they use a workflow application. It is used to distinguish different users. |  |
| `sys.app_id` | String | App ID: A unique identifier automatically assigned by the system to each App. This parameter is used to record the basic information of the current application. | This parameter is used to differentiate and locate distinct Workflow applications for users with development capabilities. |
| `sys.workflow_id` | String | Workflow ID: This parameter records information about all nodes information in the current Workflow application. | This parameter can be used by users with development capabilities to track and record information about the nodes contained within a Workflow. |
| `sys.workflow_run_id` | String | Workflow Run ID: Used to record the runtime status and execution logs of a Workflow application. | This parameter can be used by users with development capabilities to track the application’s historical execution records. |
| `sys.timestamp` | String | The start time of each workflow execution. |  |

User inputs are set at the start of each workflow run and cannot be updated.**Outputs**: Each node produces one or more outputs that can be referenced in subsequent nodes. For instance, the LLM node has outputs:![CleanShot 2025-08-04 at 14.28.57@2x.png](https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/CleanShot2025-08-04at14.28.57@2x.png?w=280&fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=22909d336858f4c30832727332f9bcd9)

CleanShot 2025-08-04 at 14.28.57@2x.png

Like inputs, node outputs cannot be updated either.**Environment Variables**: Use environment variable to store sensitive information like API keys specific to your app. This allows a clean separation between secrets and the Dify app itself, so you don’t have to risk exposing passwords and keys when sharing your app’s DSL. Environment variables are also constants and cannot be updated.**Conversation Variables (Chatflow only)**: These variables are conversation-specific — meaning they persist over multi-turn chatflow runs in a single conversatio so you can store and access dynamic information like to-do list and token cost. You can update the value of a conversation variable via the Variable Assigner node:![2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png](https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=0ef4c7277da21cce3e3463a0889fb2b1 "2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png")

### Variable Referencing

You can easily pass variables to any node when configuring its input field by selecting from a dropdown:![CleanShot 2025-08-04 at 15.13.33@2x.png](https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/CleanShot2025-08-04at15.13.33@2x.png?w=280&fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=98c80e86911741a8fe9ec99cc71785a9)

CleanShot 2025-08-04 at 15.13.33@2x.png

You can also insert variable values into complex text inputs by typing `/` slash, and selecting the desired variable from the dropdown.![image.png](https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/image.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=9889baf5b02ca41afb8607db4fddc504 "image.png")

[Previous](https://docs.dify.ai/en/use-dify/getting-started/quick-start)[User Input](https://docs.dify.ai/en/use-dify/nodes/user-input)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/user-input)