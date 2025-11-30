---
title: "Manage Apps"
source: "https://docs.dify.ai/en/use-dify/workspace/app-management"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description: "Organize, maintain, and share your AI applications with powerful management tools and best practices"
tags:
  - "clippings"
---
Managing your apps well is crucial for productive AI development. Dify provides comprehensive tools to organize, share, and maintain your applications throughout their lifecycle.

## App Organization

## Editing Application Information

Keep your apps organized with clear, descriptive information:

![Edit App Info interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/63a449e9a8ae337b9c067165d1674a45.png)

Edit App Info interface

Use consistent naming conventions across your workspace. Consider prefixes like “Draft-”, “Test-”, or “Prod-” to indicate app status.

## Creating App Variations

Duplication is perfect for creating variations or starting new projects from existing work:**When to duplicate:**
- Creating A/B test versions with different prompts or models
- Adapting an app for different audiences or use cases
- Starting a new project based on successful patterns
- Creating backups before major changes
**How duplication works:**
- All configuration, prompts, and workflows are copied
- The new app gets a default name you can customize
- Original app remains unchanged
- Both apps run independently

## App Export and Import

Dify’s DSL (Domain Specific Language) format lets you share apps between workspaces and teams:

![Export DSL interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/544c18d770e230db93d6756bba98d8a7.png)

Export DSL interface

### Exporting Applications

**Two ways to export:**
1. **From Studio page** - Click “Export DSL” in the application menu
2. **From orchestration** - Click “Export DSL” in the upper left corner
**What gets exported:**
- App configuration and metadata
- Workflow orchestration and node settings
- Model parameters and prompt templates
- Knowledge base connections (not the data itself)
**What doesn’t get exported:**
- API keys for third-party tools (security measure)
- Actual knowledge base content
- Usage logs and analytics data

If your app uses Secret-type environment variables, you’ll be asked whether to include them in the export. Be careful with sensitive information.

![Secret variables export prompt](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/25ce002ef7f0392fc6b3b6975ae137ec.png)

Secret variables export prompt

### Importing Applications

![Import application interface](https://assets-docs.dify.ai/2024/11/487d2c1cc8b86666feb35ea8a346c053.png)

Import application interface

**Import process:**
1. Upload your DSL file (YAML format)
2. System checks version compatibility
3. Warning appears if DSL version is older than current platform
4. App is created with all configurations from the file
**Version compatibility:**
- **SaaS users**: DSL files are always the latest version
- **Community users**: May need to upgrade to avoid compatibility issues

Dify DSL is the AI application engineering standard (v0.6+) that captures complete app configurations in YAML format.

## Safe App Deletion

Before deleting apps, understand the impact:**What gets deleted:**
- All app configurations and prompts
- Workflow orchestration and settings
- Usage logs and analytics
- Published web apps and API access
- All user conversations and data
**Impact on users:**
- Published web apps stop working immediately
- API calls start returning errors
- All existing user sessions are terminated

App deletion is permanent and cannot be undone. All associated data, logs, and user access will be lost immediately.

[Previous](https://docs.dify.ai/en/use-dify/workspace/plugins)[Manage Members](https://docs.dify.ai/en/use-dify/workspace/team-members-management)

[

Next

](https://docs.dify.ai/en/use-dify/workspace/team-members-management)