def summary(scores: list[float]) -> dict:
    if len(scores)==0:
        raise ValueError
    minimum=maximum=scores[0]
    mean=0.0
    for x in scores:
        if x>maximum: 
            maximum=x
        if x<minimum:
            minimum=x
        mean+=x
    scores = sorted(scores)
    n = len(scores)
    mid = n // 2
    if n % 2:
        median = scores[mid]
    else:
        median = (scores[mid - 1] + scores[mid]) / 2
    mean /= n
    return {"min": minimum, "max": maximum,"mean": mean,"median": median}
    
grades=list[float]
print(summary(grades))




