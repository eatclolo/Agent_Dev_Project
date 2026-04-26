from langchain_community.tools import Tool

from app.services.weather_service import get_weather


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


weather_tool_obj = Tool(
    name="weather_searcher",
    func=weather_tool,
    description=
    """
    Useful for retrieving weather information for a specific city.

    The input should contain a city name.

    Examples:
    - "Tokyo weather" → "Tokyo"
    - "東京天氣" → "東京"
    """

)