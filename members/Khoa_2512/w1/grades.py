def summary(scores: list[float]) -> dict:
    if len(scores)==0:
        raise ValueError
    min=max=scores[0]
    mean=median=0
    for x in scores:
        if x>max: 
            max=x
        if x<min:
            min=x
        mean+=x
    if len(scores)%2:
        median=scores[len(scores)/2]
    else:
        median=(scores[round(len(scores)/2+0.5)]+scores[round(len(scores)/2+0.5)-1])/2
    mean/=len(scores)
    return {"min": min, "max": max,"mean": mean,"median": median}
    
grades=list[float]
print(summary(grades))




