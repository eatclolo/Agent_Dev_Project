def calculate(expr: str) -> str:
    "Return the string of the expression of the calculation, return error if the error occurs"
    try:
        return str(eval(expr))
    except Exception:
        return "error"