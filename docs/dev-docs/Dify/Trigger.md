---
title: "Trigger"
source: "https://docs.dify.ai/en/use-dify/nodes/trigger/overview"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
## Introduction

Triggers are available for workflow applications only.

A trigger is a type of Start node that enables your workflow to run automatically—on a schedule or in response to events from external systems (e.g., GitHub, Gmail, or your own internal systems)—rather than waiting for active initiation from a user or an API call.Triggers are ideal for automating repetitive tasks or integrating your workflow with third-party applications to achieve automatic data synchronization and processing.A workflow can have multiple triggers running in parallel. You can also build several independent workflows on the same canvas, each starting with its own triggers.

The Sandbox plan supports up to 2 triggers per workflow. [Upgrade](https://dify.ai/pricing) to add more.

The trigger source for each workflow execution is displayed in the **Logs** section.

On Dify Cloud, trigger events (workflow executions initiated by triggers) are subject to a quota that varies by plan. For details, see the [Plan Comparison](https://dify.ai/pricing).The workspace owner and admins can check the remaining quota in **Settings** > **Billing**.

## Trigger Types

- [Schedule Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/schedule-trigger)
	- Runs your workflow at specified times or intervals.
	- Example: Automatically generate a daily sales report every morning at 9 AM and email it to your team.
- [Plugin Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/plugin-trigger)
	- Runs your workflow when a specific event occurs in an external system, via an event subscription through a trigger plugin.
	- Example: Automatically analyze and archive new messages in a specific Slack channel via a subscription to the `New Message in Channel` event through a Slack trigger plugin.
- [Webhook Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/webhook-trigger)
	- Runs your workflow when a specific event occurs in an external system via a custom webhook.
	- Example: Automatically process new orders in response to an HTTP request containing the order details from your e-commerce platform.

## Enable or Disable Triggers

In the **Quick Settings** side menu, you can enable or disable published triggers. Disabled triggers do not initiate workflow execution.

Only published triggers appear in **Quick Settings**. If you don’t see an added trigger listed, ensure it has been published first.

![Enable or Disable Published Triggers](https://mintcdn.com/dify-6c0370d8/ssHaNZ_xFtdKDTtH/images/enable_disable_added_trigger.png?w=280&fit=max&auto=format&n=ssHaNZ_xFtdKDTtH&q=85&s=9304b991518338d763e71dabb1fd4032)

Enable or Disable Published Triggers

## Test Multiple Triggers

When a workflow has multiple triggers, you can click **Test Run** > **Run all triggers** to test them at once. The first trigger that activates will initiate the workflow, and the others will then be ignored.After you click **Run all triggers**:
- Schedule triggers will run at the next scheduled execution time.
- Plugin triggers will listen for subscribed events.
- Webhook triggers will listen for external HTTP requests.

[Previous](https://docs.dify.ai/en/use-dify/nodes/user-input)[Schedule Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/schedule-trigger)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/trigger/schedule-trigger)