---
title: "Schedule Trigger"
source: "https://docs.dify.ai/en/use-dify/nodes/trigger/schedule-trigger"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
## Introduction

Triggers are available for workflow applications only.

Schedule triggers enable your workflow to run at specified times or intervals. They are ideal for recurring tasks like generating daily reports or sending scheduled notifications.

## Add a Schedule Trigger

On the workflow canvas, right-click and select **Add Node** > **Start** > **Schedule Trigger**.

- A workflow can have multiple schedule triggers running in parallel. When the parallel branches contain identical consecutive nodes, you can add a [Variable Aggregator](https://docs.dify.ai/en/use-dify/nodes/variable-aggregator) node to merge the branches before the common section, without duplicating the same nodes across each branch.

## Configure a Schedule Trigger

You can configure the schedule using either the default visual picker or a cron expression.After configuration, you can see the next 5 scheduled execution times.

Schedule triggers do not produce output variables, but they update the system variable `sys.timestamp` (the start time of each workflow execution) each time they initiate the workflow.

### With the Visual Picker

Use this for simple hourly, daily, weekly, or monthly schedules. For weekly and monthly frequencies, you can select multiple days or dates.

### With a Cron Expression

Use this for more complex and precise timing patterns, such as every 15 minutes from 9 AM to 5 PM on weekdays.

You can use LLMs to generate cron expressions.

#### Standard Format

A cron expression is a string that defines the schedule for executing your workflow. It consists of five fields separated by spaces, each representing a different time unit.

Ensure that there is a single space between each field.

```
* * * * *

| | | | |

| | | | |── Day of week (0-7 or SUN-SAT, where both 0 and 7 = Sunday)

| | | |──── Month (1-12 or JAN-DEC)

| | |────── Day of month (1-31)

| |──────── Hour (0-23)

|────────── Minute (0-59)
```

When both the **day-of-month** and **day-of-week** fields are specified, the trigger activates on dates that match *either* field.For example, `1 2 3 4 4` will trigger your workflow on the 3rd of April *and* every Thursday in April, not just on Thursdays that fall on the 3rd.

#### Special Characters

| Character | Description | Example |
| --- | --- | --- |
| `*` | Means “every”. | `*` in the **hour** field means “every hour”. |
| `,` | Separates multiple values. | `1,3,5` in the **day-of-week** field means “Monday, Wednesday, and Friday”. |
| `-` | Defines a range of values. | `9-17` in the **hour** field means “from 9 AM to 5 PM”. |
| `/` | Specifies step values. | `*/15` in the **minute** field means “every 15 minutes”. |
| `L` | Means “the last”.      In the **day-of-month** field, means “the last day of the month”.      In the **day-of-week** field: - When used alone, means “the last day of the week”. - When combined with a number, means “the last occurrence of that weekday in the month”. | `L` in the **day-of-month** field means “Jan 31, April 30, or Feb 28 in a non-leap year”.      `L` in the **day-of-week** field means Sunday.      `5L` in the **day-of-week** field means “the last Friday of the month”. |
| `?` | Means “any” or “no specific value”.      If you specify a value for the **day-of-week** field, you can use `?` for the **day-of-month** field to ignore it, and vice versa.      Not required, because `*` works as well. | To run a task every Monday, it’s more precise to set the **day-of-month** field to `?` instead of `*`. |

#### Predefined Expressions

- `@yearly`: Run once a year at 12 AM on January 1.
- `@monthly`: Run once a month at 12 AM on the first day of the month.
- `@weekly`: Run once a week at 12 AM on Sunday.
- `@daily`: Run once a day at 12 AM.
- `@hourly`: Run at the beginning of every hour.

#### Examples

## Test a Schedule Trigger

- **Run this step**: The schedule trigger runs immediately, ignoring the configured schedule.
- **Test Run**: The schedule trigger waits for its next scheduled execution time.

[Previous](https://docs.dify.ai/en/use-dify/nodes/trigger/overview)[Plugin Trigger](https://docs.dify.ai/en/use-dify/nodes/trigger/plugin-trigger)

[

Next

](https://docs.dify.ai/en/use-dify/nodes/trigger/plugin-trigger)