---
title: "Additional Features"
source: "https://docs.dify.ai/en/use-dify/build/additional-features"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
Add features to make your apps more useful. Click **Features** in the top right to add functionality.

## Workflow apps

File upload through Features is deprecated for Workflow apps. Use [file variables on the Start node](https://docs.dify.ai/en/ducmentation/pages/nodes/start) instead.

Workflow apps only support **Image Upload** via Features:**How to set it up:**
1. Enable Image Upload in Features
2. Add LLM node with vision
3. Enable VISION and select `sys.files` variable
4. Connect to End node

## Chatflow apps

Chatflow apps get more features:
- **Conversation Opener** - AI says hello first
- **Follow-up** - Suggests next questions after responses
- **Text-to-Speech** - Reads responses out loud (needs TTS setup in Model Providers)
- **File Upload** - Users can upload files
- **Citation** - Shows sources when using Knowledge Retrieval
- **Content Moderation** - Filters inappropriate content

## File upload

Most features work automatically once enabled. File upload needs more setup.**For users**: Click the paperclip icon to upload files![Upload file](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/b18af11da3f339c496193d9732906849.png)

Upload file

**For developers**: Files show up in the `sys.files` variable. Different file types need different handling:

### Documents

LLMs can’t read files directly. Use Document Extractor first.
1. Enable “Documents” in file types
2. Add Document Extractor node with `sys.files` as input
3. Add LLM node using document extractor output
4. Add Answer node with LLM output

This doesn’t remember files between conversations. Users need to re-upload each time. For persistent files, use [Start node file variables](https://docs.dify.ai/en/ducmentation/pages/nodes/start).

### Images

Some LLMs can analyze images directly.
1. Enable “Images” in file types
2. Add LLM node with VISION enabled
3. Select `sys.files` variable
4. Add Answer node with LLM output
![Enable vision](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/3a3582bd9bc8ea94bbdbfeefe6a78571.png)

Enable vision

### Mixed file types

Handle both documents and images:
1. Enable both “Images” and “Documents”
2. Add two List Operation nodes to filter file types
3. Send images to LLM with vision
4. Send documents to Document Extractor
5. Combine results in Answer node
![Mixed file types](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/66471e8e67b2ede0c94bfa1cffeab834.png)

Mixed file types

### Audio and video

LLMs can’t process these directly. You’ll need to [install](https://marketplace.dify.ai/?category=tool) use tools for audio/video processing.

## Limits

- Max 15MB per file
- Max 10 files at once

[Previous](https://docs.dify.ai/en/use-dify/build/version-control)[Single Node](https://docs.dify.ai/en/use-dify/debug/step-run)

[

Next

](https://docs.dify.ai/en/use-dify/debug/step-run)