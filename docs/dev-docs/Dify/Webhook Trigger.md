---
title: "Webhook Trigger"
source: "https://docs.dify.ai/en/use-dify/nodes/trigger/webhook-trigger"
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

A webhook allows one system to automatically send real-time data to another. When a certain event occurs, the source system packages the event details into an HTTP request and sends it to a designated URL provided by the destination system.Following the same mechanism, webhook triggers enable your workflow to run in response to third-party events. Here’s how you work with it:
1. When you add a webhook trigger to your workflow, a unique webhook URL is generated—a dedicated endpoint that listens for external HTTP requests.
	For self-hosted deployments, you can change the base prefix of this URL via the `TRIGGER_URL` environment variable.Ensure it points to a public domain or IP address accessible to external systems.
2. You use this URL to create a webhook subscribing to the events you want to monitor in an external system. Then you configure the webhook trigger to define how it processes incoming requests and extracts request data.
	For testing purposes, always use the test webhook URL to keep test data separate from production data.![Test Webhook URL](https://mintcdn.com/dify-6c0370d8/HVQw7qIn2dg_iQmO/images/test_webhook_url.png?w=280&fit=max&auto=format&n=HVQw7qIn2dg_iQmO&q=85&s=fe3a863bbae4133901e438f0d48ba65e)
	Test Webhook URL
3. When a subscribed event occurs, the external system sends an HTTP request with the event data to that provided webhook URL. Once the request is received and processed successfully, your workflow is triggered, and the specified event data is extracted into variables that can be referenced by downstream nodes.

If there’s a ready-made trigger plugin for your target external system, we recommend using the [plugin trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/plugin-trigger) instead.

## Add a Webhook Trigger

On the workflow canvas, right-click and select **Add Node** > **Start** > **Webhook Trigger**.

A workflow can have multiple webhook triggers running in parallel.When the parallel branches contain identical consecutive nodes, you can add a [Variable Aggregator](https://docs.dify.ai/en/use-dify/nodes/variable-aggregator) node to merge the branches before the common section, without duplicating the same nodes across each branch.

## Configure a Webhook Trigger

You can define how a webhook trigger handles incoming HTTP requests, including:
- The expected HTTP method for the webhook URL
- The request’s content-type
- The data you wish to extract from the request
- The response sent back to the external system when your workflow is successfully triggered

To test an unpublished webhook trigger, make sure to click **Run this step** or test-run the entire workflow first. This puts the trigger into a listening state so that it can receive external requests. Otherwise, no request will be captured.

### HTTP Method

To ensure the incoming request can be received successfully, you need to specify which HTTP method the webhook URL accepts.The method you select here must match the one used by the external system to send requests; otherwise, the requests will be rejected.

You can typically find this information in the external system’s webhook documentation or setup interface.

### Content-Type

To ensure the request body can be properly parsed and the data you need extracted, you need to specify the expected content type of the incoming request.The content-type you select here must match the content type of the request sent from the external system; otherwise, the request will be rejected.

### Query Parameters, Header Parameters, and Request Body Parameters

You can extract specific data from the query parameters, headers, and body of the incoming request. **Each extracted parameter becomes an output variable that can be used in your workflow.**Some external systems provide a delivery log for each request, where you can view all the data included in the request and decide which parameters to extract.Alternatively, you can send a test request to the webhook trigger and check the received request data in its last run logs:
1. Create a webhook in the external system using the provided test webhook URL.
2. Set the correct HTTP method and content-type in the trigger.
3. Click the **Run this step** icon. The trigger will start listening for external requests.
4. Trigger the subscribed event in the external system so it sends an HTTP request to the provided webhook URL.
5. Go to the trigger’s **Last Run** tab and check the received request data in **Input**.

The variable name you define in the trigger must match the key name of the corresponding parameter in the request.

**Parameter Settings** For each parameter to be extracted, you can specify the following:
- **Variable Name**: The key name of the parameter in the incoming request (e.g., `userID` in `userID=u-456`).
- **Data Type**: The expected data format. Available for query and request body parameters only, as header parameters are always treated as strings.
- **Required**: Whether the parameter is required for your workflow to execute properly. If any required parameter is missing from an incoming request, your workflow will not be triggered.

### Response

When your workflow is successfully triggered by an external HTTP request, a default `200 OK` response is sent back to the external system.If the external system requires a specific success response format, you can customize the status code and response body. The default one will be overridden.
- **Status Code**: Supports any status code in the range \[200, 399\].
- **Response Body**: Supports JSON or plain text.

In the returned response body, non-JSON content will be automatically converted to JSON.For example, `OK` will be wrapped as `"message": "OK"`.

## Test a Webhook Trigger

To test an unpublished webhook trigger, you must first click **Run this step** or test-run the entire workflow. This puts the trigger into a listening state so that it can receive external requests. Otherwise, incoming requests will not be captured.

[Previous](https://docs.dify.ai/en/use-dify/nodes/trigger/plugin-trigger)[LLM](https://docs.dify.ai/en/use-dify/nodes/llm)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/llm)