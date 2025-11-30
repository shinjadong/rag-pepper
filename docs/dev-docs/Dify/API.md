---
title: "API"
source: "https://docs.dify.ai/en/use-dify/publish/developing-with-apis"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Integrate your Dify workflows anywhere"
tags:
  - "clippings"
---
You can use your Dify app as a backend API service out-of-box.

## How API Integration Works

1. **Build your app** in Dify Studio with the AI capabilities you need
2. **Generate API credentials** to securely access your app’s functionality
3. **Call the API** from your application to get AI-powered responses
4. **Users interact** with your custom interface while Dify handles the AI processing

## Getting Started

Never expose API keys in frontend code or client-side requests. Always call Dify APIs from your backend to prevent abuse and maintain security.

### Text-generation application

These applications are used to generate high-quality text, such as articles, summaries, translations, etc., by calling the completion-messages API and sending user input to obtain generated text results. The model parameters and prompt templates used for generating text depend on the developer’s settings in the Dify Prompt Arrangement page.You can find the API documentation and example requests for this application in **Applications -> Access API**.For example, here is a sample call an API for text generation:

### Conversational Applications

Conversational applications facilitate ongoing dialogue with users through a question-and-answer format. To initiate a conversation, you will call the `chat-messages` API. A `conversation_id` is generated for each session and must be included in subsequent API calls to maintain the conversation flow.

> **Important Note**: The Service API does not share conversations created by the WebApp. Conversations created through the API are isolated from those created in the WebApp interface.

#### Key Considerations for conversation\_id:

- **Generating the `conversation_id`:** When starting a new conversation, leave the `conversation_id` field empty. The system will generate and return a new `conversation_id`, which you will use in future interactions to continue the dialogue.
- **Handling `conversation_id` in Existing Sessions:** Once a `conversation_id` is generated, future calls to the API should include this `conversation_id` to ensure the conversation continuity with the Dify bot. When a previous `conversation_id` is passed, any new `inputs` will be ignored. Only the `query` is processed for the ongoing conversation.
- **Managing Dynamic Variables:** If there is a need to modify logic or variables during the session, you can use conversation variables (session-specific variables) to adjust the bot’s behavior or responses.
You can access the API documentation and example requests for this application in **Applications -> Access API**.Here is an example of calling the `chat-messages` API:

[Previous](https://docs.dify.ai/en/use-dify/publish/publish-mcp)[Dashboard](https://docs.dify.ai/en/use-dify/monitor/analysis)

[

Next

](https://docs.dify.ai/en/use-dify/monitor/analysis)