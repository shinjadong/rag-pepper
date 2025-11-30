---
title: "Single Node"
source: "https://docs.dify.ai/en/use-dify/debug/step-run"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
[Skip to main content](https://docs.dify.ai/en/use-dify/debug/#content-area)

Test individual nodes or run through your workflow step-by-step to catch issues before publishing.

## Single node testing

You can test any node individually without running the entire workflow. Select the node, provide test input in its settings panel, and click Run to see the output.![](https://assets-docs.dify.ai/2025/04/376c9de6f92cb7a5f97a6661c5e0e9eb.png) After testing, click “Last run” to see execution details including inputs, outputs, timing, and any error messages.

Answer and End nodes don’t support single node testing.

## Step-by-step execution

When you run nodes one at a time, their outputs are cached in the Variable Inspector. You can edit these cached variables to test different scenarios without re-running upstream nodes.![](https://assets-docs.dify.ai/2025/06/f8656d8deeeaefeab0a8d9169f0ed2d3.png) This is useful when you want to test how a node responds to different data without having to modify and re-run all the nodes before it. Just change the variable values in the inspector and run the node again.

## Viewing execution history

Every node execution creates a record. Click “Last run” on any node to see its most recent execution details including what data went in, what came out, and how long it took.![](https://assets-docs.dify.ai/2025/04/5ee92e6406979f5101d21865f95a86e5.png)

Was this page helpful?

[Previous](https://docs.dify.ai/en/use-dify/build/additional-features)[Workflow](https://docs.dify.ai/en/use-dify/debug/variable-inspect)

[

Next

](https://docs.dify.ai/en/use-dify/debug/variable-inspect)