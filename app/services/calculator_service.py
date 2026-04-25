def calculate(expr: str) -> str:
    """
    Perform mathematical calculations.

    Args:
        expression (str): A mathematical expression, e.g., "2+2"

    Returns:
        str: The calculated result, or an error message if evaluation fails.
    """
    try:
        return str(eval(expr))
    except Exception:
        return "error"