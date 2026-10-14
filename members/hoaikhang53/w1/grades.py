def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    mean = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": mean,
        "median": round(median, 2)
    }

print(summary([7.5, 9, 6, 8]))