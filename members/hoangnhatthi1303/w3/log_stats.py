
"""Statistics for request routes and their latency."""

from collections import Counter
from math import ceil
from typing import TypedDict


class LogStats(TypedDict):
    """Summary of request counts and route latency."""

    counts: dict[str, int]
    p95: dict[str, int | float]
    slowest: str | None


def _percentile_95(values: list[int | float]) -> int | float:
    """Return the nearest-rank 95th percentile."""
    ordered = sorted(values)
    index = ceil(0.95 * len(ordered)) - 1
    return ordered[index]


def analyse(
    pairs: list[tuple[str, int | float]],
) -> LogStats:
    """Count requests by route and calculate each route's p95 latency."""
    counts = Counter(route for route, _ in pairs)
    latencies: dict[str, list[int | float]] = {}

    for route, latency in pairs:
        if latency < 0:
            raise ValueError("Latency cannot be negative")
        latencies.setdefault(route, []).append(latency)

    p95 = {
        route: _percentile_95(values)
        for route, values in latencies.items()
    }

    slowest = max(p95, key=p95.__getitem__) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
