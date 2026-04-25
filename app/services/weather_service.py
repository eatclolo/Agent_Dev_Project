def get_weather(city: str) -> str:
    """
    Return simple weather information for the given city.

    This is a mock implementation used for testing the agent and tool flow.
    It can be replaced with an external API or MCP service later.

    Args:
        city (str): Name of the city.

    Returns:
        str: A simple weather description.
    """
    return f"{city} 晴れ 20°C"