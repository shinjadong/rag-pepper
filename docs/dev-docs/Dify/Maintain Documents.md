---
title: "Maintain Documents"
source: "https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
## Manage Documentations in the Knowledge Base

### Adding Documentations

A knowledge base is a collection of documents. Documents can be uploaded by developers or operators, or synchronized from other data sources. Each document in the knowledge base corresponds to a file in its data source—for example, a Notion document or an online webpage.To upload a new document to an existing knowledge base, go to **Knowledge Base** > **Documents** and click **Add File**.![Uploading the new documentation on Knowledge Base](https://assets-docs.dify.ai/2024/12/424ab491aaebe09b490a36d26c9fa8da.png)

Uploading the new documentation on Knowledge Base

### Disable / Archive / Delete document

**Enable**: Documents that are currently in normal status can be edited and retrieved in the knowledge base. If a document has been disabled, you can re-enable it. For archived documents, you must first unarchive them before re-enabling.**Disable**: If you don’t want a document to be indexed during use, toggle off the blue switch on the right side of the document to disable it. A disabled document can still be edited or modified.**Archive**: For older documents that are no longer in use but you don’t want to delete, you can archive them. Archived documents can only be viewed or deleted and cannot be edited. You can archive a document from the Knowledge Base’s **Document List** by clicking the **Archive** button, or within the document’s details page. Archiving can be undone.**Delete**: ⚠️ Dangerous Option. For incorrect documents or clearly ambiguous content, select Delete from the menu on the right side of the document. Deleted content cannot be restored, so proceed with caution.

> The above options all support batch operations after multiple documents are selected.

![Batch file Operations](https://assets-docs.dify.ai/2024/12/5e0e64859a1ac51602d167ec55ef9350.png)

Batch file Operations

**Note:**If there are some documents in your knowledge base that haven’t been updated or retrieved for a while, the system will disable inactive documents to ensure optimal performance.
- For Sandbox users, the “inactive document disable period” is **after 7 days**.
- For Professional and Team users, it is **after 30 days**. You can revert these documents and continue using them at any time by clicking the “Enable” button in the knowledge base.
You can revert these disable documents and continue using them at any time by clicking the “Enable” button in the knowledge base. Paid users are provided with **one-click revert** function.![One-click revert](https://assets-docs.dify.ai/2024/12/bf6485b17aec716741eb65e307c2274c.png)

One-click revert

---

## Managing Text Chunks

### Viewing Text Chunks

In the knowledge base, each uploaded document is stored as text chunks. By clicking on the document title, you can view the list of chunks and their specific text content on the details page. Each page displays 10 chunks by default, but you can change the number of chunks shown per page at the bottom of the web.Only the first two lines of each content chunk are visible in the preview. If you need to see the full text within a chunk, click the “Expand Chunk” button for a complete view.![Expand text chunks](https://assets-docs.dify.ai/2024/12/86cc80f17fab1eea75aa73ee681e4663.png)

Expand text chunks

You can quickly view all enabled or disabled documents using the filter.![Filter text chunks](https://assets-docs.dify.ai/2025/01/47ef07319175a102bfd1692dcc6cac9b.png)

Filter text chunks

Different [chunking modes](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text) correspond to different text chunking preview methods:

- General Mode
- Parent-child Mode
- Q&A Mode (Community Edition Only)

**General Mode** Chunks of text in [General mode](https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text#general-mode) are independent blocks. If you want to view the complete content of a chunk, click the **full-screen** icon.![Full screen viewing](https://assets-docs.dify.ai/2024/12/c37a1a247092cda9433a10243543698f.png)

Full screen viewing

Tap the document title at the top to quickly switch to other documents in the knowledge base.![General mode - text chunking](https://assets-docs.dify.ai/2024/12/4422286c6d254e13c1ab59b147f0ffbf.png)

General mode - text chunking

---

### Checking Chunk Quality

Document chunking significantly influences the Q&A performance of knowledge-base applications. It’s recommended to perform a manual review of chunking quality before integrating the knowledge base with your application.Although automated chunk methods based on character length, identifiers, or NLP semantic system can significantly reduce the workload of large-scale text chunk, the quality of chunk is related to the text structure of different document formats and the semantic context. Manual checking and correction can effectively compensate for the shortcomings of machine chunk in semantic recognition.When checking chunk quality, pay attention to the following situations:
- **Overly short text chunks**, leading to semantic loss;
![Overly short text chunks](https://assets-docs.dify.ai/2024/12/ee081e98c1649aea4a5c2b15b88e11aa.png)

Overly short text chunks

- **Overly long text chunks**, leading to semantic noise affecting matching accuracy;
![Overly long text chunks](https://assets-docs.dify.ai/2024/12/ac47381ae4be183768dd025c37c049fa.png)

Overly long text chunks

- **Obvious semantic truncation**, which occurs when using maximum segment length limits, leading to forced semantic truncation and missing content during recall;
![Obvious semantic truncation](https://assets-docs.dify.ai/2024/12/b8ab7ac84028b0b16c3948f35015e069.png)

Obvious semantic truncation

---

### Adding Text Chunks

You can add text chunks individually to the knowledge base, and different chunking modes correspond to different ways of adding those chunks.

Adding text chunks is a paid feature. Please upgrade your account [here](https://dify.ai/pricing) to access this functionality.

- General Mode
- Parent-child Mode
- Q&A Mode (Community Edition Only)

**General Mode** Click **Add Chunks** in the chunks list page to add one or multiple custom chunks to the document.![General mode - Add chunks](https://assets-docs.dify.ai/2024/12/552ff4ab9e77130ad09aaef878b19cc9.png)

General mode - Add chunks

When manually adding text chunks, you can choose to add both the main content and keywords. After entering the content, select the **“Add another”** checkbox at the bottom to continue adding more text chunks seamlessly.![General mode - Add another text chunk](https://assets-docs.dify.ai/2024/12/cd769622bc1d85c037277ef6fa5247c9.png)

General mode - Add another text chunk

To add chunks in bulk, you need to download the upload template in CSV format first and edit all the chunk contents in Excel according to the template format, then save the CSV file and upload it.![General mode - Add customize chunks in bulk](https://assets-docs.dify.ai/2024/12/5e501dd8efba02ff31d2e739417ce864.png)

General mode - Add customize chunks in bulk

---

### Editing Text Chunks

- General Mode
- Parent-child Mode
- Q&A Mode (Community Edition Only)

**General Mode** You can directly edit or modify the added chunks content, including modifying the **text content or keywords within the chunks.**To prevent duplicate edits, an “Edited” tag will appear on the content chunk after it has been modified.![Edit text chunks](https://assets-docs.dify.ai/2024/12/92e7788dad008d38f7c8f532fbcb3636.png)

Edit text chunks

### Modify Text Chunks for Uploaded Documents

Knowledge Base supports reconfiguring document segmentation.**Larger Chunks**
- Retain more context within each chunk, ideal for tasks requiring a broader understanding of the text.
- Reduce the total number of chunks, lowering processing time and storage overhead.
**Smaller Chunks**
- Provide finer granularity, improving accuracy for tasks like extraction or summarization.
- Reduce the risk of exceeding model token limits, making it safer for models with stricter constraints.
Go to **Chunk Settings**, adjust the settings, and click **Save & Process** to save changes and reprocess the document. The chunk list will update automatically once processing is complete—no page refresh needed.![Chunk Settings](https://assets-docs.dify.ai/2025/01/36cb20be8aae1f368ebf501c0d579051.png)

Chunk Settings

![Save & Process](https://assets-docs.dify.ai/2025/01/a47b890c575a7693c40303d3d7cb4952.png)

Save & Process

---

For more details on metadata, see [*Metadata*](https://docs.dify.ai/en/use-dify/knowledge/metadata).

---

[Previous](https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/introduction)[Maintain Knowledge via API](https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-dataset-via-api)

[

Next

](https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-dataset-via-api)