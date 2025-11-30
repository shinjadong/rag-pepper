---
title: "Overview"
source: "https://docs.dify.ai/en/use-dify/workspace/readme"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description: "Workspaces are the foundational organizational unit in Dify—everything your team builds, configures, and manages exists within a workspace"
tags:
  - "clippings"
---
A workspace is your team’s complete AI environment in Dify. It contains and isolates everything your organization needs: applications, knowledge bases, team members, model configurations, plugins, and billing.

## The Workspace Mental Model

Every resource in Dify belongs to a workspace. When you create an app, it inherits the workspace’s model configurations. When you add team members, they get access to workspace resources based on their role. When you configure models or install plugins, they become available to the entire workspace.

```
🏢 Your Organization

└── 📁 Workspace

    ├── 🤖 Apps (chatbots, workflows, agents)

    ├── 📊 Knowledge Bases (documents, embeddings)

    ├── 👥 Team Members (roles & permissions) 

    ├── 🧠 Model Providers (API keys, configurations)

    ├── 🔧 Tools & Plugins (integrations, custom code)

    └── 💳 Billing (subscription, limits, usage)
```

This workspace-first design means your resources are completely isolated from other organizations, team members can only access what they’re permitted to see, and you configure models and billing once for the entire workspace.

## Workspace Creation

**Dify Cloud** automatically creates a workspace on first login. You become the owner with full permissions.**Community Edition** creates one workspace during installation. The administrator email and password are set during setup.**Multiple workspaces** are supported when you need complete isolation between different legal entities, regulatory environments, or client projects. Most organizations use a single workspace.

Your personal account can belong to multiple workspaces. Switch between them using the workspace selector in the top-left corner.

## How Resources Connect

Applications you build can use any model providers configured in the workspace, access all workspace knowledge bases, and utilize installed plugins. Team members see applications based on their workspace permissions.Workspace roles determine access across all resources:
- **Owners** control billing, model providers, and workspace settings
- **Admins** manage team members and configure models/plugins
- **Editors** build applications and manage knowledge bases
- **Members** use published applications
- **Dataset Operators** focus on knowledge base management

## Workspace Navigation

Dify organizes everything around the workspace concept. The main navigation shows Apps, Knowledge, and Tools available in your workspace. Settings contains workspace-wide configurations: Members, Model Providers, Plugins, Billing (Cloud only), and personal Account settings.

[Previous](https://docs.dify.ai/en/use-dify/knowledge/external-knowledge-api)[Model Providers](https://docs.dify.ai/en/use-dify/workspace/model-providers)

[

Next

](https://docs.dify.ai/en/use-dify/workspace/model-providers)