---
title: "Loop"
source: "https://docs.dify.ai/en/use-dify/nodes/loop"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Execute repetitive workflows with progressive refinement"
tags:
  - "clippings"
---
The Loop node executes repetitive workflows where each cycle builds on the results of the previous one. Unlike iteration, which processes array elements independently, loops create progressive workflows that evolve with each repetition.

## Loop vs Iteration

Understanding when to use each repetition pattern:

- Loop
- Iteration

**Sequential Processing** - Each cycle depends on previous results **Progressive Refinement** - Outputs improve or evolve over iterations **State Management** - Variables persist and accumulate across cycles **Use Cases** - Content refinement, problem solving, quality assurance

## Configuration

### Loop Variables

Define variables that persist across loop iterations and remain accessible after the loop completes. These variables maintain state and enable progressive workflows.

### Termination Conditions

Configure when the loop should stop executing:**Loop Termination Condition** - Expression that determines when to exit (e.g., `quality_score > 0.9`) **Maximum Loop Count** - Safety limit to prevent infinite loops **Exit Loop Node** - Immediate termination when this node is reached

The loop terminates when either the termination condition is met, the maximum count is reached, or an Exit Loop node executes. If no conditions are specified, the loop continues until the maximum count.

## Basic Loop Example

Generate random numbers until finding one less than 50:

![Basic loop workflow](https://assets-docs.dify.ai/2025/04/282013c48b46d3cc4ebf99323da10a31.png)

Basic loop workflow

Basic loop workflow for random number generation

**Workflow Steps:**
1. **Code node** generates random integers between 1-100
2. **If-Else node** checks if number is less than 50
3. **Template node** returns “done” for numbers < 50 to trigger loop termination
4. Loop continues until termination condition is met

![Loop execution steps](https://assets-docs.dify.ai/2025/04/9d9fb4db7093521000ac735a26f86962.png)

Loop execution steps

Loop execution steps and results

## Advanced Loop Example

Create a poem through iterative refinement, with each version building upon the previous one:<video controls="" src="https://assets-docs.dify.ai/2025/04/7ecfc04458aa38e721baaa5f6355486c.mp4" width="100%"></video> **Loop Variables:**
- `num` - Counter starting at 0, incrementing each iteration
- `verse` - Text variable holding the current poem version
**Workflow Logic:**
1. **If-Else node** checks if `num > 3` to determine when to exit
2. **LLM node** generates improved poem based on previous version
3. **Variable Assigner** updates both counter and poem content
4. **Exit Loop node** terminates after 4 refinement cycles
The LLM prompt references both the current verse and iteration context:

```
You are a European literary figure creating poetic verses.

Current verse: {{verse}}

Refine and improve this poem based on your previous work.
```

[Previous](https://docs.dify.ai/en/use-dify/nodes/iteration)[Code](https://docs.dify.ai/en/use-dify/nodes/code)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/code)