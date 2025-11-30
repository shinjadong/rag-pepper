---
title: "Handling Errors"
source: "https://docs.dify.ai/en/use-dify/build/predefined-error-handling-logic"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
![](https://assets-docs.dify.ai/2024/12/6e2655949889d4d162945d840d698649.png)

{% if error\_type == "rate\_limit" %} Too many requests. Please wait a moment and try again. {% else %} Something went wrong. Our team has been notified. {% endif %}

None

The default behavior. When a node fails, the whole workflow stops. You get the original error message.Use this when:
- You’re testing and want to see what broke
- The workflow can’t continue without this step

Default Value

Fail Branch

When a node fails, trigger a separate flow to handle the error.![](https://assets-docs.dify.ai/2024/12/e5ea1af947818bd9e27cab3042c1c4f3.png) The fail branch is highlighted in orange. You can:
- Send error notifications
- Try a different approach
- Log the error for debugging
- Use a backup service **Example**
Your main API fails, so the fail branch calls a backup API instead. Users never know there was a problem.

When child nodes fail inside loops and iterations, these control flow nodes have their own error behaviors.**Loop nodes** always stop immediately when any child node fails. The entire loop terminates and returns the error, preventing any further iterations from running.**Iteration nodes** let you choose how to handle child node failures through the error handling mode setting:
- `terminated` - Stops processing immediately when any item fails (default)
- `continue-on-error` - Skips the failed item and continues with the next one
- `remove-abnormal-output` - Continues processing but filters out failed items from the final output
When you set an iteration to `continue-on-error`, failed items return `null` in the output array. When you use `remove-abnormal-output`, the output array only contains successful results, making it shorter than the input array.When using default value or fail branch, you get two special variables:
- `error_type` - What kind of error happened (see [Error Types](https://docs.dify.ai/en/use-dify/build/en/use-dify/debug/error-types))
- `error_message` - The actual error details
Use these to:
- Show users helpful messages
- Send alerts to your team
- Choose different recovery strategies
- Log errors for debugging
**Example**