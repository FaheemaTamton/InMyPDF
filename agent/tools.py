from langchain.tools import Tool
from rag.vector_store import query_store


def retrieve_context(query: str) -> str:
    """
    Tool used by the agent to retrieve relevant document context.
    """
    return query_store(None, query)


retrieval_tool = Tool(
    name="DocumentRetriever",
    func=retrieve_context,
    description="Use this tool to retrieve relevant information from the ingested documents."
)
