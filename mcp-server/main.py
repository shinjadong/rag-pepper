"""
RAG Pepper MCP Server
=====================

A Model Context Protocol (MCP) server that connects Claude Desktop
to your personal RAG system powered by Dify.

This allows Claude to query your Obsidian notes through the Dify RAG pipeline.

Usage:
    1. Install dependencies: pip install -r requirements.txt
    2. Configure .env with your Dify API credentials
    3. Run: python main.py (stdio mode for Claude Desktop)
       Or: python main.py --http (HTTP mode for development)

Architecture:
    Claude Desktop -> MCP Server -> Dify API -> Supabase (pgvector)
"""

import os
import logging
from typing import Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Configuration
DIFY_API_BASE_URL = os.getenv("DIFY_API_BASE_URL", "http://localhost/v1")
DIFY_API_KEY = os.getenv("DIFY_API_KEY", "")
MCP_LOG_LEVEL = os.getenv("MCP_LOG_LEVEL", "INFO")

# Setup logging
logging.basicConfig(
    level=getattr(logging, MCP_LOG_LEVEL.upper()),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("rag-pepper-mcp")

# Initialize FastMCP server
mcp = FastMCP(
    name="rag-pepper",
    version="0.1.0",
    description="Personal RAG system for querying your Obsidian notes via Dify"
)


class DifyClient:
    """Client for interacting with Dify API."""

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    async def chat_completion(
        self,
        query: str,
        user: str = "mcp-user",
        conversation_id: Optional[str] = None,
        response_mode: str = "blocking"
    ) -> dict:
        """
        Send a chat message to Dify and get a response.

        Args:
            query: The user's question
            user: User identifier
            conversation_id: Optional conversation ID for multi-turn chat
            response_mode: 'blocking' or 'streaming'

        Returns:
            Dify API response as dict
        """
        url = f"{self.base_url}/chat-messages"
        payload = {
            "inputs": {},
            "query": query,
            "user": user,
            "response_mode": response_mode
        }

        if conversation_id:
            payload["conversation_id"] = conversation_id

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                url,
                json=payload,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def run_workflow(
        self,
        inputs: dict,
        user: str = "mcp-user",
        response_mode: str = "blocking"
    ) -> dict:
        """
        Run a Dify workflow.

        Args:
            inputs: Workflow input variables
            user: User identifier
            response_mode: 'blocking' or 'streaming'

        Returns:
            Workflow execution result
        """
        url = f"{self.base_url}/workflows/run"
        payload = {
            "inputs": inputs,
            "user": user,
            "response_mode": response_mode
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                url,
                json=payload,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()


# Initialize Dify client
dify_client = DifyClient(DIFY_API_BASE_URL, DIFY_API_KEY)


@mcp.tool()
async def query_my_notes(query: str) -> str:
    """
    Query your personal notes using RAG (Retrieval-Augmented Generation).

    This tool searches through your Obsidian notes indexed in Supabase
    and uses Dify's RAG pipeline to generate contextual answers.

    Args:
        query: Your question or search query about your notes.
               Examples:
               - "What are my notes about Python decorators?"
               - "Summarize my meeting notes from last week"
               - "What did I write about project X?"

    Returns:
        An answer based on relevant content from your notes.
    """
    if not DIFY_API_KEY:
        return (
            "Error: DIFY_API_KEY is not configured. "
            "Please set it in your .env file after creating a Dify app."
        )

    try:
        logger.info(f"Querying notes: {query[:100]}...")
        response = await dify_client.chat_completion(query)

        # Extract answer from response
        answer = response.get("answer", "")
        if not answer:
            return "No relevant information found in your notes."

        # Optionally include source metadata
        metadata = response.get("metadata", {})
        retriever_resources = metadata.get("retriever_resources", [])

        if retriever_resources:
            sources = "\n\nSources:\n"
            for idx, resource in enumerate(retriever_resources[:5], 1):
                doc_name = resource.get("document_name", "Unknown")
                score = resource.get("score", 0)
                sources += f"  {idx}. {doc_name} (relevance: {score:.2f})\n"
            answer += sources

        return answer

    except httpx.HTTPStatusError as e:
        logger.error(f"Dify API error: {e.response.status_code} - {e.response.text}")
        return f"Error querying Dify API: {e.response.status_code}"
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return f"Error: {str(e)}"


@mcp.tool()
async def search_notes(keywords: str, limit: int = 5) -> str:
    """
    Search your notes by keywords and return relevant excerpts.

    Unlike query_my_notes which generates answers, this tool returns
    raw excerpts from matching notes for direct reference.

    Args:
        keywords: Keywords to search for in your notes.
        limit: Maximum number of results to return (default: 5)

    Returns:
        A list of relevant note excerpts matching the keywords.
    """
    if not DIFY_API_KEY:
        return (
            "Error: DIFY_API_KEY is not configured. "
            "Please set it in your .env file."
        )

    try:
        logger.info(f"Searching notes for: {keywords}")

        # Use a search-focused query
        search_query = f"Find and list notes containing: {keywords}"
        response = await dify_client.chat_completion(search_query)

        answer = response.get("answer", "")
        if not answer:
            return f"No notes found matching '{keywords}'."

        return answer

    except Exception as e:
        logger.error(f"Search error: {e}")
        return f"Error searching notes: {str(e)}"


@mcp.tool()
async def get_note_summary(topic: str) -> str:
    """
    Get a summary of all your notes related to a specific topic.

    Args:
        topic: The topic to summarize (e.g., "machine learning", "project ideas")

    Returns:
        A comprehensive summary of notes related to the topic.
    """
    if not DIFY_API_KEY:
        return "Error: DIFY_API_KEY is not configured."

    try:
        logger.info(f"Summarizing notes about: {topic}")

        summary_query = (
            f"Provide a comprehensive summary of all my notes related to '{topic}'. "
            "Include key points, themes, and any actionable items."
        )
        response = await dify_client.chat_completion(summary_query)

        answer = response.get("answer", "")
        if not answer:
            return f"No notes found about '{topic}'."

        return answer

    except Exception as e:
        logger.error(f"Summary error: {e}")
        return f"Error summarizing notes: {str(e)}"


@mcp.resource("notes://status")
async def get_system_status() -> str:
    """
    Get the current status of the RAG system.

    Returns connection status to Dify and configuration information.
    """
    status_lines = [
        "RAG Pepper System Status",
        "=" * 30,
        f"Dify API URL: {DIFY_API_BASE_URL}",
        f"API Key Configured: {'Yes' if DIFY_API_KEY else 'No'}",
    ]

    if DIFY_API_KEY:
        try:
            # Test connection
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    f"{DIFY_API_BASE_URL}/parameters",
                    headers={"Authorization": f"Bearer {DIFY_API_KEY}"}
                )
                if response.status_code == 200:
                    status_lines.append("Connection Status: OK")
                else:
                    status_lines.append(f"Connection Status: Error ({response.status_code})")
        except Exception as e:
            status_lines.append(f"Connection Status: Failed ({str(e)})")
    else:
        status_lines.append("Connection Status: Not configured")

    return "\n".join(status_lines)


def main():
    """Run the MCP server."""
    import sys

    # Check for HTTP mode flag
    if "--http" in sys.argv:
        # HTTP mode for development/testing
        import uvicorn
        host = os.getenv("MCP_SERVER_HOST", "0.0.0.0")
        port = int(os.getenv("MCP_SERVER_PORT", "8000"))
        logger.info(f"Starting MCP server in HTTP mode on {host}:{port}")
        uvicorn.run(mcp.sse_app(), host=host, port=port)
    else:
        # stdio mode for Claude Desktop
        logger.info("Starting MCP server in stdio mode")
        mcp.run()


if __name__ == "__main__":
    main()
