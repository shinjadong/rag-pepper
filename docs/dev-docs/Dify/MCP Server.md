---
title: "MCP Server"
source: "https://docs.dify.ai/en/use-dify/publish/publish-mcp"
author:
  - "[[Dify Docs]]"
published:
created: 2025-11-30
description: "Expose your Dify applications as MCP servers for integration with Claude Desktop, Cursor, and other AI development tools"
tags:
  - "clippings"
---
Dify now supports exposing your applications as [MCP](https://modelcontextprotocol.io/introduction) (Model Context Protocol) servers, enabling seamless integration with AI assistants like Claude Desktop and development environments like Cursor. This allows these tools to directly interact with your Dify apps as if they were native extensions.

If you’re looking to use MCP tools within Dify workflows & agents, see [here](https://docs.dify.ai/en/use-dify/build/mcp).

## Configuring Your Dify App as an MCP Server

Navigate to your application’s configuration interface in Dify, you’ll find an MCP Server configuration module. The feature is disabled by default. When you toggle it on, Dify generates an unique MCP Server address for your application. This address serves as the connection point for external tools.

Your MCP Server URL contains authentication credentials, so treat it like an API key. If you suspect it’s been compromised, use the regenerate button to create a new URL. The old one will immediately stop working.

![CleanShot 2025-07-07 at 08.18.02.png](https://mintcdn.com/dify-6c0370d8/7ofzWAXbPyxqXN2g/images/CleanShot2025-07-07at08.18.02.png?w=280&fit=max&auto=format&n=7ofzWAXbPyxqXN2g&q=85&s=543a95cc551af0072c07713a9c819af9)

CleanShot 2025-07-07 at 08.18.02.png

## Integration with Claude Desktop

To connect your Dify app to Claude Desktop, you’ll need to add a Claude integration. Go to your Claude Profile > Settings > Integrations > Add integration. Replace the Integration URL with your Dify app’s Server URL.

## Integration with Cursor

For Cursor, create or edit the `.cursor/mcp.json` file in your project root:

```
{

  "mcpServers": {

    "your-server-name": {

      "url": "your-server-url"

    }

  }

}
```

Simply replace the URL with your Dify app’s MCP Server address. Cursor will automatically detect this configuration and make your Dify app available as a tool. You can add multiple Dify apps by including additional entries in the `mcpServers` object.

## Practical Considerations

- Descriptiveness When designing descriptions for your tool and its input parameters, think about how an AI would interpret them. Clear, specific descriptions lead to better invocations. Instead of “input data,” specify “JSON object containing user profile with required fields: name, email, preferences.”
- Latency The MCP protocol handles the communication layer, but your Dify app’s performance still matters. If your app typically takes 30 seconds to process, that latency will be felt in the client application. Consider adding progress indicators or breaking complex workflows into smaller, faster operations.

[Previous](https://docs.dify.ai/en/use-dify/publish/webapp/embedding-in-websites)[API](https://docs.dify.ai/en/use-dify/publish/developing-with-apis)

[

Next

](https://docs.dify.ai/en/use-dify/publish/developing-with-apis)