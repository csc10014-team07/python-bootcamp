import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float]]) -> dict:
    counts = Counter()
    route_latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(latency)

    p95_dict = {}
    for route, lats in route_latencies.items():
        lats.sort()
        if not lats:
            p95_dict[route] = 0.0
            continue
        idx = math.ceil(0.95 * len(lats)) - 1
        idx = max(0, min(idx, len(lats) - 1))
        p95_dict[route] = lats[idx]

    slowest = max(p95_dict, key=p95_dict.get) if p95_dict else None

    return {"counts": dict(counts), "p95": p95_dict, "slowest": slowest}
