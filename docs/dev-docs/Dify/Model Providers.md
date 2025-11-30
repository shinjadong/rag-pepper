---
title: "Model Providers"
source: "https://docs.dify.ai/en/use-dify/workspace/model-providers"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description: "Configure AI model access for your workspace—the foundation that powers all your applications"
tags:
  - "clippings"
---
Model providers give your workspace access to AI models. Every application you build needs models to function, and configuring providers at the workspace level means all team members can use them across all projects.

## System vs Custom Providers

**System Providers** are managed by Dify. You get immediate access to models without setup, billing through your Dify subscription, and automatic updates when new models become available. Best for getting started quickly.**Custom Providers** use your own API keys for direct access to model providers like OpenAI, Anthropic, or Google. You get full control, direct billing, and often higher rate limits. Best for production applications.You can use both simultaneously—system providers for prototyping, custom providers for production.

## Configure Custom Providers

Only workspace admins and owners can configure model providers. The process is consistent across providers:

## Supported Providers

**Large Language Models:**
- OpenAI (GPT-4, GPT-3.5-turbo)
- Anthropic (Claude)
- Google (Gemini)
- Cohere
- Local models via Ollama
**Embedding Models:**
- OpenAI Embeddings
- Cohere Embeddings
- Azure OpenAI
- Local embedding models
**Specialized Models:**
- Image generation (DALL-E, Stable Diffusion)
- Speech (Whisper, ElevenLabs)
- Moderation APIs

## Provider Configuration Examples

- OpenAI
- Anthropic
- Local (Ollama)

**Required:** API Key from OpenAI Platform **Optional:** Custom base URL for Azure OpenAI or proxies, Organization ID for organization-scoped usage **Available Models:** GPT-4, GPT-3.5-turbo, DALL-E, Whisper, Text embeddings

## Manage Model Credentials

Add multiple credentials for a model provider’s predefined and custom models, and easily switch between, delete, or modify these credentials.Here are some scenarios where adding multiple credentials is particularly helpful:
- **Environment Isolation**: Configure separate model credentials for different environments, such as development, testing, and production. For example, use a rate-limited credential in the development environment for debugging, and a paid credential with stable performance and a sufficient quota in the production environment to ensure service quality.
- **Cost Optimization**: Add and switch between multiple credentials from different accounts or model providers to maximize the use of free or low-cost quotas, thereby reducing application development and operational costs.
- **Model Testing**: During model fine-tuning or iteration, you may create multiple model versions. By adding credentials for these different versions, you can quickly switch between them to test and evaluate their performance.

Use multiple credentials to configure load balancing for a model.

- Predefined Model
- Custom Model

After installing a model provider and configuring the first credential, click **Config** in the upper-right corner to perform the following actions:
- Add a new credential
- Select a credential as the default for all predefined models
- Edit a credential
- Delete a credential

If the default credential is deleted, you must manually specify a new one.

![Manage credentials for predefined models](https://mintcdn.com/dify-6c0370d8/DLsSss2CKEMuNxH2/images/predefined_model_credential.png?w=280&fit=max&auto=format&n=DLsSss2CKEMuNxH2&q=85&s=c3a961de219bf20c476239957fddeb7a)

Manage credentials for predefined models

## Configure Model Load Balancing

Load balancing is a paid feature. You can enable it through [a paid SaaS subscription or an Enterprise license](https://dify.ai/pricing).

Model providers typically enforce rate limits on API access within a specific timeframe to ensure stability and fair use. For enterprise applications, a high volume of concurrent requests from a single credential can easily trigger these limits, disrupting user access.An effective solution is load balancing, which distributes request traffic across multiple model credentials. This prevents rate limit issues and single points of failure, ensuring business continuity and faster response times for all users.Dify employs a round-robin strategy for load balancing, sequentially routing model requests to each credential in the load balancing pool. If a credential hits a rate limit, it is temporarily removed from rotation for one minute to avoid futile retries.To configure load balancing for a model, follow these steps:
1. In the model list, find the target model, click the corresponding **Config**, and select **Load balancing**.
2. In the load balancing pool, click **Add credential** to select from existing credentials or add a new one.

**Default Config** refers to the default credential currently specified for that model.

![Add credentials for load balancing](https://mintcdn.com/dify-6c0370d8/7Ipos5aBzrNU-g5O/images/add_load_balancing_credential.png?w=280&fit=max&auto=format&n=7Ipos5aBzrNU-g5O&q=85&s=d7f48a7820d0af3bcc9ad7f24b051710)

Add credentials for load balancing

1. Enable at least two credentials in the load balancing pool, then click **Save**. Models with load balancing enabled will be marked with a special icon.
![Load balancing icon](https://mintcdn.com/dify-6c0370d8/-0brHWfkawXPDZZK/images/load_balancing_icon.png?w=280&fit=max&auto=format&n=-0brHWfkawXPDZZK&q=85&s=1dc66baca22603f71122be8c035529a7)

Load balancing icon

When you switch from load-balancing mode back to the default single-credential mode, your load-balancing configuration is preserved for future use.

## Access and Billing

System providers are billed through your Dify subscription with usage limits based on your plan. Custom providers bill you directly through the provider (OpenAI, Anthropic, etc.) and often provide higher rate limits.Team access follows workspace permissions:
- **Owners/Admins** can configure, modify, and remove providers
- **Editors/Members** can view available providers and use them in applications

API keys are stored securely but grant workspace-wide model access. Only give admin privileges to trusted team members who should have billing responsibility.

## Troubleshooting

**Authentication Failed:** Verify API key accuracy, check expiration, ensure sufficient credits, confirm key permissions.**Model Not Available:** Check provider configuration includes the model, verify API key tier access, refresh provider settings.**Rate Limits:** Upgrade provider account, implement request queuing, consider custom providers for higher limits.

[Previous](https://docs.dify.ai/en/use-dify/workspace/readme)[Plugins](https://docs.dify.ai/en/use-dify/workspace/plugins)

[

Next

](https://docs.dify.ai/en/use-dify/workspace/plugins)