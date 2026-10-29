import math
from collections import Counter, defaultdict


def _calculate_p95(latencies: list[float | int]) -> float:
    sorted_lat = sorted(latencies)
    n = len(sorted_lat)
    index = math.ceil(0.95 * n) - 1
    return float(sorted_lat[index])


def analyse(pairs: list[tuple[str, float | int]]) -> dict:
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    counts = Counter()
    grouped_latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        grouped_latencies[route].append(latency)

    p95_dict = {
        route: _calculate_p95(lats) for route, lats in grouped_latencies.items()
    }

    slowest_route = max(p95_dict, key=p95_dict.get)

    return {"counts": counts, "p95": p95_dict, "slowest": slowest_route}
