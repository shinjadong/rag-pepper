---
title: "Template"
source: "https://docs.dify.ai/en/use-dify/nodes/template"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Transform and format data using Jinja2 templating"
tags:
  - "clippings"
---
The Template node transforms and formats data from multiple sources into structured text using Jinja2 templating. Use it to combine variables, format outputs, and prepare data for downstream nodes or end users.

![Template node interface](https://assets-docs.dify.ai/2025/04/0838bb5c7e1d1a58ed30fcd9fc48920f.png)

Template node interface

Template node configuration interface

## Jinja2 Templating

Template nodes use Jinja2 templating syntax to create dynamic content that adapts based on workflow data. This provides programming-like capabilities including loops, conditionals, and filters for sophisticated text generation.

### Variable Substitution

Reference workflow variables using double curly braces: `{{ variable_name }}`. You can access nested object properties and array elements using dot notation and bracket syntax.

```
{{ user.name }}

{{ items[0].title }}

{{ data.metrics.score }}
```

### Conditional Logic

Show different content based on data values using if-else statements:

```
{% if user.subscription == 'premium' %}

Welcome back, Premium Member! You have access to all features.

{% else %}

Consider upgrading to Premium for additional capabilities.

{% endif %}
```

### Loops and Iteration

Process arrays and objects with for loops to generate repetitive content:

```
{% for item in search_results %}

### Result {{ loop.index }}

**Score**: {{ item.score | round(2) }}

{{ item.content }}

---

{% endfor %}
```

![Template formatting example](https://assets-docs.dify.ai/2025/04/0ae3f13cf725cb2c52c72cc354e592ee.png)

Template formatting example

Template processing knowledge retrieval results

## Data Formatting

### Filters

Jinja2 filters transform data during template rendering:

```
{{ name | upper }}

{{ price | round(2) }}

{{ content | replace('\n', '<br>') }}

{{ timestamp | strftime('%B %d, %Y') }}

{{ score | default('No score available') }}
```

Handle missing or invalid data gracefully using default values and conditional checks:

```
{{ user.email | default('No email provided') }}

{{ metrics.accuracy | round(2) if metrics.accuracy else 'Not calculated' }}
```

## Interactive Forms

Templates can generate interactive HTML forms for structured data collection in chat interfaces:

```
<form data-format="json">

  <label for="username">Username:</label>

  <input type="text" name="username" required />

  

  <label for="priority">Priority:</label>

  <input type="select" name="priority" data-options='["low","medium","high"]'/>

  

  <label for="message">Message:</label>

  <textarea name="message" placeholder="Enter your message"></textarea>

  

  <input type="checkbox" name="urgent" data-tip="Mark as urgent"/>

  <button data-variant="primary">Submit</button>

</form>
```

![Interactive form rendering](https://assets-docs.dify.ai/2025/04/9d24e9cfa3cdde00e4eee15bd4bbea76.png)

Interactive form rendering

Interactive form rendered in chat interface

When users submit forms, responses become structured JSON data available for immediate processing in downstream workflow nodes.

## Output Limits

Template output is limited to **80,000 characters** (configurable via `TEMPLATE_TRANSFORM_MAX_LENGTH`). This prevents memory issues and ensures reasonable processing times for large template outputs.

[Previous](https://docs.dify.ai/en/use-dify/nodes/code)[Variable Aggregator](https://docs.dify.ai/en/use-dify/nodes/variable-aggregator)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/variable-aggregator)