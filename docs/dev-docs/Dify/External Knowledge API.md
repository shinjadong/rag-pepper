---
title: "External Knowledge API"
source: "https://docs.dify.ai/en/use-dify/knowledge/external-knowledge-api"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
## Endpoint

```
POST <your-endpoint>/retrieval
```

This API is used to connect to a knowledge base that is independent of the Dify and maintained by developers. For more details, please refer to [Connecting to an External Knowledge Base](https://docs.dify.ai/guides/knowledge-base/connect-external-knowledge-base). You can use `API-Key` in the `Authorization` HTTP Header to verify permissions. The authentication logic is defined by you in the retrieval API, as shown below:

```
Authorization: Bearer {API_KEY}
```

## Request Body Elements

The request accepts the following data in JSON format.The `retrieval_setting` property is an object containing the following keys:The `metadata_condition` property is an object containing the following keys:Each object in the `conditions` array contains the following keys:Supported `comparison_operator` operators:
- `contains`: Contains a certain value
- `not contains`: Does not contain a certain value
- `start with`: Starts with a certain value
- `end with`: Ends with a certain value
- `is`: Equals a certain value
- `is not`: Does not equal a certain value
- `empty`: Is empty
- `not empty`: Is not empty
- `=`: Equals
- `≠`: Not equal
- `>`: Greater than
- `<`: Less than
- `≥`: Greater than or equal to
- `≤`: Less than or equal to
- `before`: Before a certain date
- `after`: After a certain date

## Request Syntax

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.The following data is returned in JSON format by the service.The `records` property is a list object containing the following keys:

## Response Syntax

```
HTTP/1.1 200

Content-type: application/json

{

    "records": [{

                    "metadata": {

                            "path": "s3://dify/knowledge.txt",

                            "description": "dify knowledge document"

                    },

                    "score": 0.98,

                    "title": "knowledge.txt",

                    "content": "This is the document for external knowledge."

            },

            {

                    "metadata": {

                            "path": "s3://dify/introduce.txt",

                            "description": "dify introduce"

                    },

                    "score": 0.66,

                    "title": "introduce.txt",

                    "content": "The Innovation Engine for GenAI Applications"

            }

    ]

}
```

## Errors

If the action fails, the service sends back the following error information in JSON format:The `error_code` property has the following types:

### HTTP Status Codes

**AccessDeniedException** The request is denied because of missing access permissions. Check your permissions and retry your request. HTTP Status Code: 403 **InternalServerException** An internal server error occurred. Retry your request. HTTP Status Code: 500

## Development Example

You can learn how to develop external knowledge base plugins through the following video tutorial using LlamaCloud as an example:For more information about how it works, please refer to the plugin’s [GitHub repository](https://github.com/langgenius/dify-official-plugins/tree/main/extensions/llamacloud).

[Previous](https://docs.dify.ai/en/use-dify/knowledge/connect-external-knowledge-base)[Overview](https://docs.dify.ai/en/use-dify/workspace/readme)

[

Next

](https://docs.dify.ai/en/use-dify/workspace/readme)