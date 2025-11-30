---
title: "Maintain Knowledge via API"
source: "https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-dataset-via-api"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
> The authentication and invocation methods for the Knowledge Base API are consistent with the Application Service API. However, a single Knowledge Base API token generated has the authority to operate on all visible knowledge bases under the same account. Please pay attention to data security.

### Advantages of Utilizing Knowledge Base API

Leveraging the API for knowledge base maintenance significantly enhances data processing efficiency. It enables seamless data synchronization via command-line interfaces, facilitating automated operations instead of manipulating the user interface.Key advantages include:
- Automated Synchronization: Enables seamless integration between data systems and the Dify knowledge base, fostering efficient workflow construction.
- Comprehensive Management: Offers functionalities such as knowledge base listing, document enumeration, and detailed querying, facilitating the development of custom data management interfaces.
- Flexible Content Ingestion: Accommodates both plain text and file upload methodologies, supporting batch operations for addition and modification of content chunks.
- Enhanced Productivity: Minimizes manual data handling requirements, thereby optimizing the overall user experience on the Dify platform.

### How to Use

Navigate to the knowledge base page, and you can switch to the **API ACCESS** page from the left navigation. On this page, you can view the dataset API documentation provided by Dify and manage the credentials for accessing the dataset API in **API Keys**.![Knowledge API Document](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/knowledge-base/knowledge-and-documents-maintenance/2848fc9fc3a7f641f16eee11ed6c6223.png)

Knowledge API Document

### API Requesting Examples

#### Create a document from text

This api is based on an existing Knowledge and creates a new document through text based on this Knowledge.Request example:Response example:

```
{

  "document": {

    "id": "",

    "position": 1,

    "data_source_type": "upload_file",

    "data_source_info": {

        "upload_file_id": ""

    },

    "dataset_process_rule_id": "",

    "name": "text.txt",

    "created_from": "api",

    "created_by": "",

    "created_at": 1695690280,

    "tokens": 0,

    "indexing_status": "waiting",

    "error": null,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "archived": false,

    "display_status": "queuing",

    "word_count": 0,

    "hit_count": 0,

    "doc_form": "text_model"

  },

  "batch": ""

}
```

#### Create a Document from a file

This API is based on an existing knowledge and creates a new document through a file based on this knowledge.

```
{

  "document": {

    "id": "",

    "position": 1,

    "data_source_type": "upload_file",

    "data_source_info": {

      "upload_file_id": ""

    },

    "dataset_process_rule_id": "",

    "name": "Dify.txt",

    "created_from": "api",

    "created_by": "",

    "created_at": 1695308667,

    "tokens": 0,

    "indexing_status": "waiting",

    "error": null,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "archived": false,

    "display_status": "queuing",

    "word_count": 0,

    "hit_count": 0,

    "doc_form": "text_model"

  },

  "batch": ""

}
```

#### Create Documents from a File

This api is based on an existing Knowledge and creates a new document through a file based on this Knowledge.Request example:Response example:

```
{

  "document": {

    "id": "",

    "position": 1,

    "data_source_type": "upload_file",

    "data_source_info": {

      "upload_file_id": ""

    },

    "dataset_process_rule_id": "",

    "name": "Dify.txt",

    "created_from": "api",

    "created_by": "",

    "created_at": 1695308667,

    "tokens": 0,

    "indexing_status": "waiting",

    "error": null,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "archived": false,

    "display_status": "queuing",

    "word_count": 0,

    "hit_count": 0,

    "doc_form": "text_model"

  },

  "batch": ""

}
```

#### Create an Empty Knowledge Base

Only used to create an empty knowledge base.

Request example:Response example:

```
{

  "id": "",

  "name": "name",

  "description": null,

  "provider": "vendor",

  "permission": "only_me",

  "data_source_type": null,

  "indexing_technique": null,

  "app_count": 0,

  "document_count": 0,

  "word_count": 0,

  "created_by": "",

  "created_at": 1695636173,

  "updated_by": "",

  "updated_at": 1695636173,

  "embedding_model": null,

  "embedding_model_provider": null,

  "embedding_available": null

}
```

#### Get Knowledge Base List

Request example:Response example:

```
{

  "data": [

    {

      "id": "",

      "name": "name",

      "description": "desc",

      "permission": "only_me",

      "data_source_type": "upload_file",

      "indexing_technique": "",

      "app_count": 2,

      "document_count": 10,

      "word_count": 1200,

      "created_by": "",

      "created_at": "",

      "updated_by": "",

      "updated_at": ""

    },

    ...

  ],

  "has_more": true,

  "limit": 20,

  "total": 50,

  "page": 1

}
```

#### Delete a Knowledge Base

Request example:Response example:

```
204 No Content
```

#### Update a Document with Text

This api is based on an existing Knowledge and updates the document through text based on this Knowledge Request example:Response example:

```
{

  "document": {

    "id": "",

    "position": 1,

    "data_source_type": "upload_file",

    "data_source_info": {

      "upload_file_id": ""

    },

    "dataset_process_rule_id": "",

    "name": "name.txt",

    "created_from": "api",

    "created_by": "",

    "created_at": 1695308667,

    "tokens": 0,

    "indexing_status": "waiting",

    "error": null,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "archived": false,

    "display_status": "queuing",

    "word_count": 0,

    "hit_count": 0,

    "doc_form": "text_model"

  },

  "batch": ""

}
```

#### Update a document with a file

This api is based on an existing Knowledge, and updates documents through files based on this Knowledge.Request example:Response example:

```
{

  "document": {

    "id": "",

    "position": 1,

    "data_source_type": "upload_file",

    "data_source_info": {

      "upload_file_id": ""

    },

    "dataset_process_rule_id": "",

    "name": "Dify.txt",

    "created_from": "api",

    "created_by": "",

    "created_at": 1695308667,

    "tokens": 0,

    "indexing_status": "waiting",

    "error": null,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "archived": false,

    "display_status": "queuing",

    "word_count": 0,

    "hit_count": 0,

    "doc_form": "text_model"

  },

  "batch": "20230921150427533684"

}
```

#### Get Document Embedding Status (Progress)

Request example:Response example:

```
{

  "data":[{

    "id": "",

    "indexing_status": "indexing",

    "processing_started_at": 1681623462.0,

    "parsing_completed_at": 1681623462.0,

    "cleaning_completed_at": 1681623462.0,

    "splitting_completed_at": 1681623462.0,

    "completed_at": null,

    "paused_at": null,

    "error": null,

    "stopped_at": null,

    "completed_segments": 24,

    "total_segments": 100

  }]

}
```

#### Delete a Document

Request example:Response example:

```
{

  "result": "success"

}
```

#### Get the Document List of a Knowledge Base

Request example:Response example:

```
{

  "data": [

    {

      "id": "",

      "position": 1,

      "data_source_type": "file_upload",

      "data_source_info": null,

      "dataset_process_rule_id": null,

      "name": "dify",

      "created_from": "",

      "created_by": "",

      "created_at": 1681623639,

      "tokens": 0,

      "indexing_status": "waiting",

      "error": null,

      "enabled": true,

      "disabled_at": null,

      "disabled_by": null,

      "archived": false

    },

  ],

  "has_more": false,

  "limit": 20,

  "total": 9,

  "page": 1

}
```

#### Add Chunks to a Document

Request example:Response example:

```
{

  "data": [{

    "id": "",

    "position": 1,

    "document_id": "",

    "content": "1",

    "answer": "1",

    "word_count": 25,

    "tokens": 0,

    "keywords": [

        "a"

    ],

    "index_node_id": "",

    "index_node_hash": "",

    "hit_count": 0,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "status": "completed",

    "created_by": "",

    "created_at": 1695312007,

    "indexing_at": 1695312007,

    "completed_at": 1695312007,

    "error": null,

    "stopped_at": null

  }],

  "doc_form": "text_model"

}
```

#### Get Chunks from a Document

Request example:Response example:

```
{

  "data": [{

    "id": "",

    "position": 1,

    "document_id": "",

    "content": "1",

    "answer": "1",

    "word_count": 25,

    "tokens": 0,

    "keywords": [

        "a"

    ],

    "index_node_id": "",

    "index_node_hash": "",

    "hit_count": 0,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "status": "completed",

    "created_by": "",

    "created_at": 1695312007,

    "indexing_at": 1695312007,

    "completed_at": 1695312007,

    "error": null,

    "stopped_at": null

  }],

  "doc_form": "text_model"

}
```

#### Delete a Chunk in a Document

Request example:Response example:

```
{

  "result": "success"

}
```

#### Update a Chunk in a Document

Request example:Response example:

```
{

  "data": [{

    "id": "",

    "position": 1,

    "document_id": "",

    "content": "1",

    "answer": "1",

    "word_count": 25,

    "tokens": 0,

    "keywords": [

        "a"

    ],

    "index_node_id": "",

    "index_node_hash": "",

    "hit_count": 0,

    "enabled": true,

    "disabled_at": null,

    "disabled_by": null,

    "status": "completed",

    "created_by": "",

    "created_at": 1695312007,

    "indexing_at": 1695312007,

    "completed_at": 1695312007,

    "error": null,

    "stopped_at": null

  }],

  "doc_form": "text_model"

}
```

#### Retrieve Chunks from a Knowledge Base

Request example:Response example:

```
{

  "query": {

    "content": "test"

  },

  "records": [

    {

      "segment": {

        "id": "7fa6f24f-8679-48b3-bc9d-bdf28d73f218",

        "position": 1,

        "document_id": "a8c6c36f-9f5d-4d7a-8472-f5d7b75d71d2",

        "content": "Operation guide",

        "answer": null,

        "word_count": 847,

        "tokens": 280,

        "keywords": [

          "install",

          "java",

          "base",

          "scripts",

          "jdk",

          "manual",

          "internal",

          "opens",

          "add",

          "vmoptions"

        ],

        "index_node_id": "39dd8443-d960-45a8-bb46-7275ad7fbc8e",

        "index_node_hash": "0189157697b3c6a418ccf8264a09699f25858975578f3467c76d6bfc94df1d73",

        "hit_count": 0,

        "enabled": true,

        "disabled_at": null,

        "disabled_by": null,

        "status": "completed",

        "created_by": "dbcb1ab5-90c8-41a7-8b78-73b235eb6f6f",

        "created_at": 1728734540,

        "indexing_at": 1728734552,

        "completed_at": 1728734584,

        "error": null,

        "stopped_at": null,

        "document": {

          "id": "a8c6c36f-9f5d-4d7a-8472-f5d7b75d71d2",

          "data_source_type": "upload_file",

          "name": "readme.txt",

          "doc_type": null

        }

      },

      "score": 3.730463140527718e-05,

      "tsne_position": null

    }

  ]

}
```

Request example:Response example:

```
{

    "id": "9f63c91b-d60e-4142-bb0c-c81a54dc2db5",

    "type": "string",

    "name": "test"

}
```

Request example:Response example:

```
{

  "id": "abc",

  "type": "string",

  "name": "test",

}
```

Request example:Response example:

```
200 success
```

#### Enable/Disable Built-in Fields in the Knowledge Base

Request example:Response example:

```
200 success
```

Request example:Response example:

```
200 success
```

Request example:Response example:

```
{

  "doc_metadata": [

    {

      "id": "550e8400-e29b-41d4-a716-446655440000",

      "type": "string",

      "name": "title",

      "use_count": 42

    },

    {

      "id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",

      "type": "number",

      "name": "price",

      "use_count": 28

    },

    {

      "id": "7ba7b810-9dad-11d1-80b4-00c04fd430c9",

      "type": "time",

      "name": "created_at",

      "use_count": 35

    }

  ],

  "built_in_field_enabled": true

}
```

Response example:

```
{

    "code": "no_file_uploaded",

    "message": "Please upload your file.",

    "status": 400

  }
```

[Previous](https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents)[Metadata](https://docs.dify.ai/en/use-dify/knowledge/metadata)

[

Next

](https://docs.dify.ai/en/use-dify/knowledge/metadata)