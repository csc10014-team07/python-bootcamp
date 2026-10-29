def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("scores cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    median = round(median, 2)

    return {"min": minimum, "max": maximum, "mean": mean, "median": median}


def main():
    scores = [3.0, 1.0, 4.0, 2.0]
    print(summary(scores))


if __name__ == "__main__":
    main()
