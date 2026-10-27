from collections import Counter
from math import ceil


def analyse(pairs) -> dict:
    """Analyse request counts and p95 latency for each route."""
    counts = Counter()
    latencies = {}

    # Collect request counts and latencies for each route
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency_ms)

    # Calculate p95 latency for each route
    p95 = {}

    for route, values in latencies.items():
        values.sort()
        index = ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    # Find the route with the highest p95 latency
    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
