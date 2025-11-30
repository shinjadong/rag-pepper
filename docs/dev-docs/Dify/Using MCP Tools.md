---
title: "Using MCP Tools"
source: "https://docs.dify.ai/en/use-dify/build/mcp"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
Connect external tools from [MCP servers](https://modelcontextprotocol.io/introduction) to your Dify apps. Instead of just built-in tools, you can use tools from the growing [MCP ecosystem](https://mcpservers.org/).

This covers using MCP tools in Dify. To publish Dify apps as MCP servers, see [here](https://docs.dify.ai/en/use-dify/publish/publish-mcp).

Only supports MCP servers with [HTTP transport](https://modelcontextprotocol.io/docs/concepts/architecture#transport-layer) right now.

## Adding MCP servers

Go to **Tools** → **MCP** in your workspace.![](https://mintcdn.com/dify-6c0370d8/7ofzWAXbPyxqXN2g/images/6cef1436fcc13a65ccedb54bcf5ab77eb87b8faba1098a85951839fb1907f2d2.png?fit=max&auto=format&n=7ofzWAXbPyxqXN2g&q=85&s=65d4b39cec4a998480db2c8a1ed36831) Click **Add MCP Server (HTTP)**:![](https://mintcdn.com/dify-6c0370d8/7ofzWAXbPyxqXN2g/images/b5429131836c1caae84f4ce8b3b806221e39636723644961ce2f2a97d5421f16.png?fit=max&auto=format&n=7ofzWAXbPyxqXN2g&q=85&s=dca573eca5488cc2b52f6e30eefb8dac) **Server URL**: Where the MCP server lives (like `https://api.notion.com/mcp`) **Name & Icon**: Call it something useful. Dify tries to grab icons automatically.**Server ID**: Unique identifier (lowercase, numbers, underscores, hyphens, max 24 chars)

Never change the server ID once you start using it. This will break any apps that use tools from this server.

## What happens next

Dify automatically:
1. Connects to the server
2. Handles any OAuth stuff
3. Gets the list of available tools
4. Makes them available in your app builder
You’ll see a server card once it finds tools:![](https://mintcdn.com/dify-6c0370d8/7ofzWAXbPyxqXN2g/images/fcef5ecad1deca82a1d8988c4bcb7cec745a0cd47945ff05fca588502cfaafbc.png?fit=max&auto=format&n=7ofzWAXbPyxqXN2g&q=85&s=ff64850c089ed5b06b64449f681f5e69)

## Managing servers

Click any server card to:**Update Tools**: Refresh when the external service adds new tools ![](https://mintcdn.com/dify-6c0370d8/7ofzWAXbPyxqXN2g/images/7b526a64ff34b10a357511b2cd3e42f251a6786210eac71c58ca7bfccdf63f0c.png?fit=max&auto=format&n=7ofzWAXbPyxqXN2g&q=85&s=79785739094935dd3e0fd18c3975de33) **Re-authorize**: Fix auth when tokens expire **Edit Settings**: Change server details (but not the ID!) **Remove**: Disconnect the server (this breaks apps using its tools)

## Using MCP tools

Once connected, MCP tools show up everywhere you’d expect:**In agents**: Tools appear grouped by server (“Notion MCP » Create Page”) **In workflows**: MCP tools become available as nodes **In agent nodes**: Same as regular agents

## Customizing tools

When you add an MCP tool, you can customize it:![](https://mintcdn.com/dify-6c0370d8/7ofzWAXbPyxqXN2g/images/CleanShot2025-07-07at07.41.33@2x.png?fit=max&auto=format&n=7ofzWAXbPyxqXN2g&q=85&s=73042add2d9b4ec78771b1fd7fc7e899) **Description**: Override the default description to be more specific **Parameters**: For each tool parameter, choose:
- **Auto**: Let the AI decide the value
- **Fixed**: Set a specific value that never changes
**Example**: For a search tool, set `numResults` to 5 (fixed) but keep `query` on auto.

## Sharing apps

When you export apps that use MCP tools:
- The export includes server IDs
- To use the app elsewhere, add the same servers with identical IDs
- Document which MCP servers your app needs

## Troubleshooting

**“Unconfigured Server”**: Check the URL and re-authorize **Missing tools**: Hit “Update Tools” **Broken apps**: You probably changed a server ID. Add it back with the original ID.

## Tips

- Use permanent, descriptive server IDs like `github-prod` or `crm-system`
- Keep the same MCP setup across dev/staging/production
- Set fixed values for config stuff, auto for dynamic inputs
- Test MCP integrations before deploying

[Previous](https://docs.dify.ai/en/use-dify/build/predefined-error-handling-logic)[Version Control](https://docs.dify.ai/en/use-dify/build/version-control)

[

Next

](https://docs.dify.ai/en/use-dify/build/version-control)