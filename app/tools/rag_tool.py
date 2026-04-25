from app.services.rag_service import search_knowledge
from langchain_community.tools import Tool

def rag_tool(query: str) -> str:
    """
    Retrieve relevant information from a knowledge base.

    This is a placeholder for future RAG (Retrieval-Augmented Generation)
    integration. The implementation will be replaced with an actual
    retrieval pipeline.

    Args:
        query (str): User query.

    Returns:
        str: Retrieved information (currently a placeholder response).
    """
    return search_knowledge(query)


rag_tool_obj = Tool(
    name="knowledge_searcher",
    func=rag_tool,
    description=
    """
    Useful for answering general knowledge questions or retrieving information from a knowledge base.

    Use this tool when the question is not about calculation or weather.

    Examples:
    - "What is RAG?" 
    - "Explain machine learning"
    """
)