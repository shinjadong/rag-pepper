---
title: "Phoenix"
source: "https://docs.dify.ai/en/use-dify/monitor/integrations/integrate-phoenix"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
### What is Phoenix

Open-source & OpenTelemetry-based observability, evaluation, prompt engineering and experimentation platform for your LLM workflows and agents.

For more details, please refer to [Phoenix](https://phoenix.arize.com/).

---

### How to Configure Phoenix

#### 2\. Get your Phoenix API Key

Retrieve your Phoenix API Key from the user menu at the top-right. Click on **API Key**, then on the API Key to copy it:![Phoenix API Key](https://i.ibb.co/pB1W0pk8/dify-docs-phoenix-api-key.png)

Phoenix API Key

#### 3\. Integrating Phoenix with Dify

Configure Phoenix in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.![Tracing app performance](https://i.ibb.co/gMmXxfhQ/dify-docs-phoenix-in-use.png)

Tracing app performance

After clicking configure, paste the **API Key** and **project name** created in Phoenix into the configuration and save.![Configure Phoenix](https://i.ibb.co/jv6QFbp7/dify-docs-phoenix-config.png)

Configure Phoenix

Once successfully saved, you can view the monitoring status on the current page.![Configure Phoenix](https://i.ibb.co/HTJsj9x2/dify-docs-phoenix-in-service.png)

Configure Phoenix

### How to Configure Phoenix Cloud

#### 2\. Create your Phoenix Space

You can create your Phoenix Space from the user menu at the top-right. Click on **Create Space**, then provide a unique URL identifier for your space:![Phoenix Cloud Create Space](https://i.ibb.co/7JYPzZBf/dify-docs-phoenix-cloud-create-space.png)

Phoenix Cloud Create Space

Once successfully saved, you can view the space status on the overview page.![Phoenix Cloud Space Overview](https://i.ibb.co/Z6RqMhhq/dify-docs-phoenix-cloud-space-overview.png)

Phoenix Cloud Space Overview

#### 3\. Create your Phoenix API Key

After launching your space, you can create your Phoenix API Key from the **Settings** option in the user menu at the bottom-left. Click on **System Key**, then provide a name for your Phoenix API Key:![Phoenix Cloud API Key](https://i.ibb.co/SXMyX9K3/dify-docs-phoenix-cloud-api-key.png)

Phoenix Cloud API Key

#### 4\. Integrating Phoenix Cloud with Dify

Configure Phoenix in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.![Tracing app performance](https://i.ibb.co/gMmXxfhQ/dify-docs-phoenix-in-use.png)

Tracing app performance

After clicking configure, paste the **API Key** and **project name** along with **Space Hostname** created in Phoenix Cloud into the configuration and save.![Configure Phoenix](https://i.ibb.co/jv6QFbp7/dify-docs-phoenix-config.png)

Configure Phoenix

Once successfully saved, you can view the monitoring status on the current page.![Configure Phoenix](https://i.ibb.co/HTJsj9x2/dify-docs-phoenix-in-service.png)

Configure Phoenix

### Monitoring Data List

#### Workflow/Chatflow Trace Information

**Used to track workflows and chatflows**

| Workflow | Phoenix Trace |
| --- | --- |
| workflow\_app\_log\_id/workflow\_run\_id | id |
| user\_session\_id | \- placed in metadata |
| workflow\_ | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage\_metadata |
| metadata | metadata |
| error | error |
| \[workflow\] | tags |
| ”conversation\_id/none for workflow” | conversation\_id in metadata |

**Workflow Trace Info**
- workflow\_id - Unique identifier of the workflow
- conversation\_id - Conversation ID
- workflow\_run\_id - ID of the current run
- tenant\_id - Tenant ID
- elapsed\_time - Time taken for the current run
- status - Run status
- version - Workflow version
- total\_tokens - Total tokens used in the current run
- file\_list - List of processed files
- triggered\_from - Source that triggered the current run
- workflow\_run\_inputs - Input data for the current run
- workflow\_run\_outputs - Output data for the current run
- error - Errors encountered during the current run
- query - Query used during the run
- workflow\_app\_log\_id - Workflow application log ID
- message\_id - Associated message ID
- start\_time - Start time of the run
- end\_time - End time of the run
- workflow node executions - Information about workflow node executions
- Metadata
	- workflow\_id - Unique identifier of the workflow
	- conversation\_id - Conversation ID
	- workflow\_run\_id - ID of the current run
	- tenant\_id - Tenant ID
	- elapsed\_time - Time taken for the current run
	- status - Run status
	- version - Workflow version
	- total\_tokens - Total tokens used in the current run
	- file\_list - List of processed files
	- triggered\_from - Source that triggered the current run

#### Message Trace Information

**Used to track LLM-related conversations**

| Chat | Phoenix LLM |
| --- | --- |
| message\_id | id |
| user\_session\_id | \- placed in metadata |
| ”llm” | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage\_metadata |
| metadata | metadata |
| \[“message”, conversation\_mode\] | tags |
| conversation\_id | conversation\_id in metadata |

**Message Trace Info**
- message\_id - Message ID
- message\_data - Message data
- user\_session\_id - User session ID
- conversation\_model - Conversation mode
- message\_tokens - Number of tokens in the message
- answer\_tokens - Number of tokens in the answer
- total\_tokens - Total number of tokens in the message and answer
- error - Error information
- inputs - Input data
- outputs - Output data
- file\_list - List of processed files
- start\_time - Start time
- end\_time - End time
- message\_file\_data - File data associated with the message
- conversation\_mode - Conversation mode
- Metadata
	- conversation\_id - Conversation ID
	- ls\_provider - Model provider
	- ls\_model\_name - Model ID
	- status - Message status
	- from\_end\_user\_id - ID of the sending user
	- from\_account\_id - ID of the sending account
	- agent\_based - Whether the message is agent-based
	- workflow\_run\_id - Workflow run ID
	- from\_source - Message source

#### Moderation Trace Information

**Used to track conversation moderation**

| Moderation | Phoenix Tool |
| --- | --- |
| user\_id | \- placed in metadata |
| “moderation” | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| \[“moderation”\] | tags |

**Moderation Trace Info**
- message\_id - Message ID
- user\_id: User ID
- workflow\_app\_log\_id - Workflow application log ID
- inputs - Moderation input data
- message\_data - Message data
- flagged - Whether the content is flagged for attention
- action - Specific actions taken
- preset\_response - Preset response
- start\_time - Moderation start time
- end\_time - Moderation end time
- Metadata
	- message\_id - Message ID
	- action - Specific actions taken
	- preset\_response - Preset response

#### Suggested Question Trace Information

**Used to track suggested questions**

| Suggested Question | Phoenix LLM |
| --- | --- |
| user\_id | \- placed in metadata |
| ”suggested\_question” | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| \[“suggested\_question”\] | tags |

**Message Trace Info**
- message\_id - Message ID
- message\_data - Message data
- inputs - Input content
- outputs - Output content
- start\_time - Start time
- end\_time - End time
- total\_tokens - Number of tokens
- status - Message status
- error - Error information
- from\_account\_id - ID of the sending account
- agent\_based - Whether the message is agent-based
- from\_source - Message source
- model\_provider - Model provider
- model\_id - Model ID
- suggested\_question - Suggested question
- level - Status level
- status\_message - Status message
- Metadata
	- message\_id - Message ID
	- ls\_provider - Model provider
	- ls\_model\_name - Model ID
	- status - Message status
	- from\_end\_user\_id - ID of the sending user
	- from\_account\_id - ID of the sending account
	- workflow\_run\_id - Workflow run ID
	- from\_source - Message source

#### Dataset Retrieval Trace Information

**Used to track knowledge base retrieval**

| Dataset Retrieval | Phoenix Retriever |
| --- | --- |
| user\_id | \- placed in metadata |
| ”dataset\_retrieval” | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| \[“dataset\_retrieval”\] | tags |
| message\_id | parent\_run\_id |

**Dataset Retrieval Trace Info**
- message\_id - Message ID
- inputs - Input content
- documents - Document data
- start\_time - Start time
- end\_time - End time
- message\_data - Message data
- Metadata
	- message\_id - Message ID
	- ls\_provider - Model provider
	- ls\_model\_name - Model ID
	- status - Message status
	- from\_end\_user\_id - ID of the sending user
	- from\_account\_id - ID of the sending account
	- agent\_based - Whether the message is agent-based
	- workflow\_run\_id - Workflow run ID
	- from\_source - Message source

#### Tool Trace Information

**Used to track tool invocation**

| Tool | Phoenix Tool |
| --- | --- |
| user\_id | \- placed in metadata |
| tool\_name | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| \[“tool”, tool\_name\] | tags |

#### Tool Trace Info

- message\_id - Message ID
- tool\_name - Tool name
- start\_time - Start time
- end\_time - End time
- tool\_inputs - Tool inputs
- tool\_outputs - Tool outputs
- message\_data - Message data
- error - Error information, if any
- inputs - Inputs for the message
- outputs - Outputs of the message
- tool\_config - Tool configuration
- time\_cost - Time cost
- tool\_parameters - Tool parameters
- file\_url - URL of the associated file
- Metadata
	- message\_id - Message ID
	- tool\_name - Tool name
	- tool\_inputs - Tool inputs
	- tool\_outputs - Tool outputs
	- tool\_config - Tool configuration
	- time\_cost - Time cost
	- error - Error information, if any
	- tool\_parameters - Tool parameters
	- message\_file\_id - Message file ID
	- created\_by\_role - Role of the creator
	- created\_user\_id - User ID of the creator
**Generate Name Trace Information** **Used to track conversation title generation**

| Generate Name | Phoenix Tool |
| --- | --- |
| user\_id | \- placed in metadata |
| ”generate\_conversation\_name” | name |
| start\_time | start\_time |
| end\_time | end\_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| \[“generate\_name”\] | tags |

**Generate Name Trace Info**
- conversation\_id - Conversation ID
- inputs - Input data
- outputs - Generated conversation name
- start\_time - Start time
- end\_time - End time
- tenant\_id - Tenant ID
- Metadata
	- conversation\_id - Conversation ID
	- tenant\_id - Tenant ID

[Previous](https://docs.dify.ai/en/use-dify/monitor/integrations/integrate-opik)[W&B Weave](https://docs.dify.ai/en/use-dify/monitor/integrations/integrate-weave)

[

Next

](https://docs.dify.ai/en/use-dify/monitor/integrations/integrate-weave)