def approx_pi(n_terms: int) -> float:
    """Approximate the value of π using the Leibniz formula.

    The Leibniz formula for π states that:
    π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

    This function computes the approximation using the first `n_terms` terms
    of the series.

    Args:
        n_terms (int): The number of terms to include in the approximation.

    Returns:
        float: The approximate value of π.
    """
    pi_approximation = 0.0
    for k in range(n_terms):
        term = (-1) ** k / (2 * k + 1)
        pi_approximation += term
    pi_approximation *= 4
    return pi_approximation