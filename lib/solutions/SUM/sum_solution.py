# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    """
    Adds two positive integers. Input parameters must be between 0 and 100.

    Args:
        x (int): a positive integer between 0-100
        y (int): a positive integer between 0-100

    Returns:
        int: an Integer representing the sum of the two numbers
    """
    
    if 0 <= x <= 100 and 0 <= y <= 100:
        return x + y
    else:
        raise ValueError("Input parameters must be positive integers 0 and 100")
