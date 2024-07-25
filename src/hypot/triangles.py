"""File to calculate hypotenuse of a triangle"""

# Requirements

# 2 inputs, positive, int or float (is digit)
# 1 output, float
# External library? Not allowed
# Function sqrt(a^2 + b^2)
# Secondary function for sqrt : positive float in, return float


def hypot(opp: float, adj: float) -> float:
    """Calculate hypotenuse of right angle triangle

    Args:
        a (float): Length of the opposite
        b (float): Length of the adjacent

    Returns:
        float: Length of the hypotenuse
    """
    return sqrt(opp**2 + adj**2)

def sqrt(val:float) -> float:
    """Return square root

    Args:
        val (float): Input

    Returns:
        float: Output
    """
    return val ** 0.5


print(hypot(3, 4))
