---
title: "Access Control"
source: "https://docs.dify.ai/en/use-dify/publish/webapp/web-app-access"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
Web app access controls who can use your published applications. By default, new apps are restricted to specific team members—you choose exactly who gets access.

Only Workspace Owner, Admin, and Editor roles can create and publish web apps.

Configure access from the Studio → Web App Access Permissions, or from the Publish panel when editing your app.Dify Enterprise offers four access levels:![](https://assets-docs.dify.ai/2025/06/323f40cbf4d0091bc84724fd0bee529c.png)

### All Members Within Platform

Any member of your Dify Enterprise workspace can access the app. Users must authenticate with their workspace credentials—password, verification code, or SSO.Members can access the app through the direct URL or the workspace Explorer page.

If you upgraded from Dify Enterprise v2.7.x or earlier with Web App SSO enabled, your apps automatically switched to **Authenticated External Users** permission during the v2.8.x upgrade.

### Specific Members Within Platform

**Default setting for new apps.** Restricts access to chosen groups or individual members within your workspace. Perfect for department-specific tools or sensitive data applications.

Without any groups or members selected, nobody can access your app—including you.

Configure access by groups or individuals:

- By Groups
- By Individuals

Add entire groups for automatic permission management. When someone joins the group, they get app access. When they leave, access is revoked.![](https://assets-docs.dify.ai/2025/06/2ae6a255c949c0e28ab2acd087db9b62.png)

Workspace Owners, Admins, and Editors can always edit any app in the workspace. However, they still need to be explicitly added to the access list to use the published web app.

### Authenticated External Users

Users outside your Dify Enterprise workspace can access the app through SSO authentication. Admins manage external users through third-party identity providers, keeping them separate from internal workspace data.

## Large Enterprises

IT builds apps, other departments use them without joining Dify

## External Partners

Provide AI services to suppliers, contractors, or clients

## Customer Support

Public-facing tools for product help and consultation

If this option is disabled, ask your Dify administrator to configure Web App External User Authentication.

### Anyone

**No authentication required.** Anyone with the URL can access your app immediately. Use for public demos, customer tools, or open resources.

## Finding Your Apps

Team members see all accessible apps in the workspace Explorer page:![](https://assets-docs.dify.ai/2025/04/44a22b6f66f80eae805a307388e5b3e9.png)

## Common Questions

View current permissions in the **Who can access web app** section of your app’s publish settings.

No. API access is controlled separately by API keys. Changing web app permissions doesn’t affect existing API functionality.

[Previous](https://docs.dify.ai/en/use-dify/publish/webapp/web-app-settings)[Embeds](https://docs.dify.ai/en/use-dify/publish/webapp/embedding-in-websites)

[

Next

](https://docs.dify.ai/en/use-dify/publish/webapp/embedding-in-websites)