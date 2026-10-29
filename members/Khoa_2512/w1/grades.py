"""Calculate summary statistics for a list of scores."""

from typing import TypedDict


class ScoreSummary(TypedDict):
    """Represent summary statistics for a set of scores."""

    min: float
    max: float
    mean: float
    median: float


def summary(scores: list[float]) -> ScoreSummary:
    """Calculate the minimum, maximum, mean, and median of scores.

    Args:
        scores: A non-empty list of numeric scores.

    Returns:
        A dictionary containing the minimum, maximum, mean, and median,
        with the mean and median rounded to two decimal places.

    Raises:
        ValueError: If the scores list is empty.
    """
    if len(scores) == 0:
        raise ValueError("scores must not be empty")

    minimum = maximum = scores[0]
    mean = 0.0

    for x in scores:
        maximum = max(maximum, x)
        minimum = min(minimum, x)
        mean += x

    scores = sorted(scores)
    n = len(scores)
    mid = n // 2

    if n % 2:
        median = scores[mid]
    else:
        median = (scores[mid - 1] + scores[mid]) / 2

    mean /= n

    return {
        "min": minimum,
        "max": maximum,
        "mean": round(mean, 2),
        "median": round(median, 2),
    }


grades: list[float] = []
print(summary(grades))
