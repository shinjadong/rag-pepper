---
title: "Manage Members"
source: "https://docs.dify.ai/en/use-dify/workspace/team-members-management"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description: "Manage workspace members, roles, and permissions to build effective AI teams"
tags:
  - "clippings"
---
Team management in Dify is workspace-centric. When you add members to your workspace, they get access to workspace resources based on their assigned role. Understanding these roles helps you build secure, productive AI teams.

## Team Size Limits

Your workspace can include different numbers of team members based on your Dify edition:
- **Free:** 1 member (solo development)
- **Professional:** 3 members (small teams)
- **Team:** Unlimited members (growing companies)
- **Community/Enterprise:** Unlimited members (self-hosted)

## Workspace Roles

Owner

**Full workspace control.** Only one owner per workspace. Controls all team members, billing, model providers, and can delete the workspace. Cannot transfer ownership to another member.

Admin

Editor

**Application development.** Can create, edit, and delete applications, manage knowledge bases, and use all workspace tools. Cannot manage team members or configure providers.

Member

**Application usage only.** Can use published applications and tools they have access to. Cannot create or modify applications.

Dataset Operator

**Knowledge base specialist.** Focused role for managing datasets and knowledge bases. Can create and manage knowledge bases but has limited application access.

## Adding Team Members

Only workspace owners can invite new team members:

Community Edition requires email service configuration before invitations work properly.

## Member Management

**Removing Members:** Only workspace owners can remove team members. When removed, members immediately lose workspace access, but applications they created remain in the workspace.**Role Changes:** Only workspace owners can modify member roles. Role changes take effect immediately and alter what the member can access across the workspace.**Multiple Workspaces:** Team members can belong to multiple workspaces. They switch between workspaces using the selector in the top-left corner.

## Access Patterns

**Resource Inheritance:** All workspace resources (model providers, plugins, knowledge bases) are available to team members based on their role permissions.**Application Access:** Members see applications based on sharing settings and their role. Owners and Admins see all applications. Editors see applications they can modify. Members see only published applications they’re permitted to use.**Configuration Access:** Model providers and plugins configured at the workspace level become available to all applications created by team members with appropriate permissions.

[Previous](https://docs.dify.ai/en/use-dify/workspace/app-management)[Personal Settings](https://docs.dify.ai/en/use-dify/workspace/personal-account-management)

[

Next

](https://docs.dify.ai/en/use-dify/workspace/personal-account-management)