def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    mean = sum(sorted_scores) / n

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(sorted_scores),
        "max": max(sorted_scores),
        "mean": round(mean, 2),
        "median": round(median, 2),
    }

print(summary([7.5, 9, 6, 8]))