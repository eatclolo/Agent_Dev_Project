from langchain_community.tools import Tool

from app.services.calculator_service import calculate


def calculator_tool(query: str) -> str:
    """
    Perform mathematical calculations.

    Args:
        query (str): A mathematical expression. e.g., "2+2"

    Returns:
        str: str: The calculated result, or  "error" if evaluation fails.
    """
    return calculate(query)


calculator_tool_obj = Tool(
    name="Calculator",
    func=calculator_tool,
    description=
    """
    Useful for solving mathematical expressions.

    Extract and evaluate only the mathematical expression from the user's input.

    Examples:
    - "2+2" → "2+2"
    - "what is 10 * 5" → "10*5"
    - "我要計算1+1" → "1+1"
    """
)
