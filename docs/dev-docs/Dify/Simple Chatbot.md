---
title: "Simple Chatbot"
source: "https://docs.dify.ai/en/use-dify/tutorials/simple-chatbot"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description: "Hello World"
tags:
  - "clippings"
---
The real value of Dify lies in how easily you can build, deploy, and scale an idea no matter how complex. It’s built for fast prototyping, smooth iteration, and reliable deployment at any level.Let’s start by learning reliable LLM integration into your applications. In this guide, you’ll build a simple chatbot that classifies the user’s question, respond directly using the LLM, and enhance the response with a country-specific fun fact.![](https://www.youtube.com/watch?v=dJ34OU_JY7Y)

## Step 1: Create a New Workflow (2 min)

1. Go to **Studio** > **Workflow** > **Create from Blank** > **Orchestrate** > **New Chatflow** > **Create**

## Step 2: Add Workflow Nodes (6 min)

When you want to reference any variable, type `{` or `/` first and you can see the different variables available in your workflow.

### 1\. LLM Node and Output: Understand and Answer the Question

`LLM` node sends a prompt to a language model to generate a response based on user input. It abstracts away the complexity of API calls, rate limits, and infrastructure, so you can just focus on designing logic.

### 2\. Code Block: Get Fun Fact

`Code` node executes custom logic using code. It lets you inject code exactly where needed—within a visual workflow—saving you from wiring up an entire backend.

### 3\. Answer Node: Final Answer to User

`Answer` Node creates a clean final output to return.

End Workflow:![Complete workflow diagram showing LLM, Code, and Answer nodes connected](https://mintcdn.com/dify-6c0370d8/MiGqQWUuc2Ca3g05/images/quick-start-workflow-overview.png?w=280&fit=max&auto=format&n=MiGqQWUuc2Ca3g05&q=85&s=c1b6d3fea100561e75c09c18e80df0c8)

Complete workflow diagram showing LLM, Code, and Answer nodes connected

---

## Step 3: Test the Bot (3 min)

Click `Preview`, then ask:
- “What is the capital of France?”
- “Tell me about Japanese cuisine”
- “Describe the culture in Italy”
- Any other questions
Make sure your Bot works as expected!

## You’ve Completed the Bot!

This guide showed how to integrate language models reliably and scalably without reinventing infrastructure. With Dify’s visual workflows and modular nodes, you’re not just building faster, you’re adopting a clean, production-ready architecture for LLM-powered apps.