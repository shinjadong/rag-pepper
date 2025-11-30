---
title: "If-Else"
source: "https://docs.dify.ai/en/use-dify/nodes/ifelse"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Add conditional logic and branching to workflows"
tags:
  - "clippings"
---
The If-Else node adds decision-making logic to your workflows by routing execution down different paths based on conditions you define. It evaluates variables and determines which branch your workflow should follow.

![Text summary workflow with conditional logic](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d26ffff1b2ad0989d46e80d6812cf2e7.png)

Text summary workflow with conditional logic

If-Else conditional branching example

## Branching Logic

The node supports multiple branching paths to handle complex decision trees:**IF Path** executes when the primary condition evaluates to true.**ELIF Paths** provide additional conditions to check in sequence when the IF condition is false. You can add multiple ELIF branches for complex logic.**ELSE Path** serves as the fallback when no conditions match, ensuring your workflow always has a path to follow.

## Condition Types

Configure conditions to test variables using various comparison operators:

- Text Operations
- Value Checks

**Contains** / **Not contains** - Check if text includes specific words or phrases **Starts with** / **Ends with** - Test text beginnings or endings for pattern matching **Is** / **Is not** - Exact value matching for precise text comparison

## Complex Conditions

Combine multiple conditions using logical operators for sophisticated decision-making:

![Multiple Condition Judgments](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/0b71ee7363e07298348e0c81e63481b0.png)

Multiple Condition Judgments

Complex condition configuration with AND/OR logic

**AND Logic** requires all conditions to be true. Use this when you need multiple criteria to be met simultaneously.**OR Logic** requires any condition to be true. Use this when you want to trigger the same action for different scenarios.

## Variable References

Reference any variable from previous workflow nodes in your conditions. Variables can come from user input, LLM responses, API calls, or any other workflow node output.Use the variable selector to choose from available variables, or type variable names directly using the `{{variable_name}}` syntax.

[Previous](https://docs.dify.ai/en/use-dify/nodes/question-classifier)[Iteration](https://docs.dify.ai/en/use-dify/nodes/iteration)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/iteration)