---
title: "Plugins"
source: "https://docs.dify.ai/en/use-dify/workspace/plugins"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description: "Extend Dify with custom models, tools, and integrations through modular components"
tags:
  - "clippings"
---
Plugins are how Dify connects to everything—model providers, external APIs, custom tools. They’re modular components that extend your workspace capabilities that you install once but can use everywhere.![](https://mintcdn.com/dify-6c0370d8/MiGqQWUuc2Ca3g05/images/plugins-tab.png?fit=max&auto=format&n=MiGqQWUuc2Ca3g05&q=85&s=2572299ff6c6bbf31f4a9718de7f107e) Access plugin management through the Plugins tab in your workspace.

## How Plugins Work

![](https://mintcdn.com/dify-6c0370d8/MiGqQWUuc2Ca3g05/images/plugin-management.png?fit=max&auto=format&n=MiGqQWUuc2Ca3g05&q=85&s=3869e637fe3ddaab2268d9f944ce8468) Plugins are workspace-scoped. When you install a plugin, every application in your workspace can use it. Team members access plugins based on their roles:

## Installing Plugins

## Marketplace

Official and partner plugins, tested and maintained

## GitHub

Install from any public repository with URL + version

## Local Upload

Custom.zip packages for private or internal plugins

## What Plugins Really Are

Think of plugins as the bridge between Dify and the outside world:

## Model Providers

Every LLM in Dify (OpenAI, Anthropic, etc.) is actually a plugin

## Tools & Functions

API calls, data processing, calculations—all plugin-based

## Custom Endpoints

Expose your Dify apps as APIs that external systems can call

## Reverse Invocation

Plugins can call back into Dify to use models, tools, or workflows

## Workspace Plugin Settings

Control plugin permissions in your workspace settings:

Installation Rights

Debug Access

**Everyone** - All members can debug plugin issues **Admin Only** - Restrict debugging to admins

Auto-updates

Choose update strategy (security only vs. all updates) and specify which plugins to include or exclude

After installing, most plugins need configuration—API keys, endpoints, or service settings. These apply workspace-wide.

## Plugin Installation Restrictions

Enterprise Only

In enterprise workspaces, you might see installation restrictions when browsing the plugin marketplace:**What you’ll encounter:**
- The “Install Plugin” dropdown in Plugins → Explore Marketplace may show limited options
- Installation confirmation dialogs will indicate if a plugin is blocked by policy
- When importing apps with plugins (DSL files), you’ll see notices about restricted plugins
**Plugin badges in marketplace:**![](https://assets-docs.dify.ai/2025/06/c2bfdfbb2132848e589073600e55ffab.png) Look for these badges to identify plugin types—your workspace may only allow certain types based on admin settings.

If you can’t install a needed plugin, contact your workspace admin. They control which plugin sources (marketplace, GitHub, local files) and types (official, partner, third-party) are allowed.

## Building Custom Plugins

Develop plugins using Dify’s SDK when you need custom functionality:
1. Get a debugging key from Settings → Plugins → Debugging
2. Build and test your plugin locally
3. Package as a.zip with manifest and dependencies
4. Distribute privately or publish to the marketplace