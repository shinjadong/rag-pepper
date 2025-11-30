---
title: "Chat Web Apps"
source: "https://docs.dify.ai/en/use-dify/publish/webapp/chatflow-webapp"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Turn your chatflow into a fully-featured conversation interface with persistent history and interactive features"
tags:
  - "clippings"
---
Chat web apps transform your chatflow into a complete conversation experience. Users get persistent chat sessions, smart interactions, and all the features you’ve configured—without installing anything.

## How Chat Apps Work

Your chatflow automatically becomes a web app when you publish it. The system creates a responsive interface that:
- **Maintains conversation context** across user sessions
- **Inherits all orchestration settings** from your chatflow configuration
- **Adapts to any screen size** from mobile to desktop
- **Handles user authentication** if you’ve enabled access controls

Unlike single-use text generators, chat apps maintain conversation memory and let users build on previous exchanges.

## Interactive Features

Your web app automatically includes these capabilities based on your chatflow settings:

## Pre-conversation Setup

When your chatflow uses variables, users complete a form before chatting starts. This front-loads context gathering instead of interrupting the conversation flow.

![Pre-conversation variable form](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/8decae00eeea24622e1f2ef73d4c447e.png)

Pre-conversation variable form

Here’s how the user experience works:

## Conversation Experience

Once chatting begins, users get an interface designed for natural interaction:

![Chat interface with response options](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/5b7a6f950ed8a2ce3a705f362b4813fe.png)

Chat interface with response options

Every AI response includes these actions:
- **Copy button** - One-click copying for easy sharing or note-taking
- **Feedback buttons** - Like/dislike ratings to improve your app over time
- **Follow-up suggestions** - AI generates 3 contextually relevant next questions

## Session Management

Users can manage multiple conversation threads like modern messaging apps:

![Conversation management sidebar](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/46372ad4d79a3ea943d43f9434974956.png)

Conversation management sidebar

**Conversation Controls:**
- **Start new** - Begin fresh conversations without losing context from previous ones
- **Pin important** - Keep crucial conversations accessible at the top of the list
- **Delete finished** - Clean up conversations that are no longer relevant

Each conversation thread maintains its own memory and context. Users can seamlessly switch between different topics or projects.

## Conversation Openers

Enable conversation openers to eliminate the intimidating blank chat screen:

![AI conversation opener message](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/22e59e509296d25eb85cbd541e161c6d.png)

AI conversation opener message

When users start new conversations, the AI proactively introduces itself and explains its capabilities. This immediately shows users what they can accomplish and increases engagement.

Conversation openers work especially well for specialized apps where users might not know all available features.

## Follow-up Questions

The system automatically generates contextual follow-up questions after each AI response:

![Follow-up question suggestions](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/f88a7ffd777d51299f8b604249c044b3.png)

Follow-up question suggestions

These suggestions are:
- **Contextually relevant** to the current conversation topic
- **Dynamically generated** based on the AI’s response
- **Clickable shortcuts** that help users explore deeper or pivot to related topics

## Voice Input

Speech-to-text transforms your chat app into a voice-first experience:

![Speech-to-text microphone button](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/3a64c79792f1166301403f6c44cf4c85.png)

Speech-to-text microphone button

**How it works:**
1. The microphone button appears when you enable speech-to-text in your chatflow
2. Users click to start recording their question
3. Speech converts to text in real-time as they speak
4. They can edit the text before sending or send immediately

Users must grant microphone permissions in their browser. The app will prompt for this permission when they first try to use voice input.

## Source Citations

When your app references knowledge bases or external content, citations show users exactly where information comes from:Citations build user trust by providing transparency about information sources. Users can click through to verify details or explore source materials further.

For detailed citation setup, see [Citation and Attribution](https://docs.dify.ai/en/use-dify/knowledge/retrieval-test-and-citation).

[Previous](https://docs.dify.ai/en/use-dify/publish/webapp/workflow-webapp)[Settings](https://docs.dify.ai/en/use-dify/publish/webapp/web-app-settings)

[

Next

](https://docs.dify.ai/en/use-dify/publish/webapp/web-app-settings)