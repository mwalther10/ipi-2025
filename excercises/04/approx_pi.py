import math


def approx_pi(n_approx: int) -> float:
    """Approximate the value of π using the Leibniz formula.

    The Leibniz formula for π states that:
    π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

    This function computes the n-th approximation of π using the Leibniz series.

    Args:
        n_approx (int): The approximation step to compute.

    Returns:
        float: The approximate value of π.
    """
    pi_approximation = 0.0
    for k in range(n_approx + 1):
        term = (-1) ** k / (2 * k + 1)
        pi_approximation += term
    pi_approximation *= 4
    return pi_approximation


assert math.isclose(approx_pi(0), 4)
assert math.isclose(approx_pi(1), 2.666666666666667)
assert math.isclose(approx_pi(2), 3.466666666666667)
assert math.isclose(approx_pi(78), 3.1542503744801236)
assert math.isclose(approx_pi(1000), 3.1425916543395442)
assert math.isclose(approx_pi(10000), 3.1416926435905346)
