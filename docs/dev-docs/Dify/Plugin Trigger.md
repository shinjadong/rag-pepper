---
title: "Plugin Trigger"
source: "https://docs.dify.ai/en/use-dify/nodes/trigger/plugin-trigger"
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

A plugin trigger automatically initiates your workflow when a specific event occurs in an external system. All you need to do is subscribe to these events through a trigger plugin and add the corresponding plugin trigger to your workflow.For example, suppose you have installed a GitHub trigger plugin. It provides a list of GitHub events you can subscribe to, including `Pull Request`, `Push`, and `Issue`. If you subscribe to the `Pull Request` event and add the `Pull Request` plugin trigger to your workflow, it will automatically run whenever someone opens a pull request in the specified repository.

## Add and Configure a Plugin Trigger

1. On the workflow canvas, right-click and select **Add Node** > **Start**, then choose from the available plugin triggers or search for more in [Dify Marketplace](https://marketplace.dify.ai/?language=en-US&category=trigger).
2. Select an existing subscription or [create a new one](https://docs.dify.ai/en/use-dify/nodes/trigger/#create-a-new-subscription).
	View how many workflows are using a specific subscription from the plugin’s details panel under **Plugins**.
3. Configure any other required settings.

The output variables of a plugin trigger are defined by its trigger plugin and cannot be modified.

## Create a New Subscription

A subscription cannot be modified once created. To make changes, delete the existing one and create a new subscription.

A trigger plugin supports creating up to 10 subscriptions per workspace.

Each subscription is built on a webhook. When you create a subscription, you’re essentially setting up a webhook that listens for events from an external system.

A webhook allows one system to automatically send real-time data to another. When a certain event occurs, the source system packages the event details into an HTTP request and sends it to a designated URL provided by the destination system.

Dify supports the following two methods for creating subscriptions (webhooks), but the options available in each plugin depend on how that plugin was designed.
- **Automatic Creation**: You select the events you want to subscribe to, and Dify automatically creates the corresponding webhook in the external system. This requires prior authorization via **OAuth** or **API keys** so Dify can handle the webhook setup on your behalf.
- **Manual Creation**: You create the webhook yourself using the webhook callback URL provided by Dify. No authorization is needed.
![Ways to Create Subscriptions](https://mintcdn.com/dify-6c0370d8/ssHaNZ_xFtdKDTtH/images/create_subscription_method.png?w=280&fit=max&auto=format&n=ssHaNZ_xFtdKDTtH&q=85&s=395b1ee713bd4f4af22712b3c3185004)

Ways to Create Subscriptions

- Create with OAuth (Automatic)
- Create with API Key (Automatic)

On Dify Cloud, many popular trigger plugins are pre-configured with default OAuth clients so you can authorize Dify with a single click.For self-hosted deployments, only the custom OAuth client option is available, meaning that you need to create the OAuth application yourself in the external system.

The displayed **Callback URL** is used internally by Dify to create the webhook in the external system on your behalf, so you don’t need to take any action with this URL.For self-hosted deployments, you can change the URL’s base prefix via the `TRIGGER_URL` environment variable. Ensure it points to a public domain or IP address accessible to external systems.

## Test a Plugin Trigger

To test an unpublished plugin trigger, you must first click **Run this step** or test-run the entire workflow. This puts the trigger into a listening state so that it can monitor external events. Otherwise, the trigger will not capture subscribed events even when they occur.

[Previous](https://docs.dify.ai/en/use-dify/nodes/trigger/schedule-trigger)[Webhook Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/webhook-trigger)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/trigger/webhook-trigger)