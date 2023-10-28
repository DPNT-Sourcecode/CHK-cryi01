# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    """
    Description

    Args:

    Returns:
    """
    
    if 0 <= x <= 100 and 0 <= y <= 100:
        return x + y
    else:
        raise ValueError("Input parameters must be positive integers 0 and 100")



