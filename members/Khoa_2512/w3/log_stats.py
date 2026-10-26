from collections import Counter, defaultdict
from math import ceil
def p95(latencies_list: list[float |int])->float:
    temp=sorted(latencies_list)
    length= len(latencies_list)
    pos=ceil(0.95*length)-1
    return float(temp[pos])

def analyse(pairs: list[tuple[str, float|int]]) ->dict:
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}
    counts=Counter()
    latencies_list=defaultdict(list)
    for route, latencies in pairs:
        counts[route]+=1
        latencies_list[route].append(latencies)

    p95s={
        route: p95(latency)for route, latency in latencies_list.items()
    }
    slowest= max(p95s, key=p95s.get)

    return {"counts": counts, "p95": p95s, "slowest": slowest}
    
        