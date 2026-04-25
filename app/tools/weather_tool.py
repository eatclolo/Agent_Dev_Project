from app.services.weather_service import get_weather
from langchain_community.tools import Tool

def weather_tool(query: str) -> str:
    """
    Return simple weather information for the given city.

    This is a mock implementation used for testing the agent and tool flow.
    It can be replaced with an external API or MCP service later.

    Args:
        query (str): Name of the city.

    Returns:
        str: A simple weather description.
    """
    return get_weather(query)


calculator_tool_obj = Tool(
    name="weather_searcher",
    func=weather_tool,
    description="Return simple weather information for the given city."
)