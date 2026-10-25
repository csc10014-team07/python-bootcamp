from collections import Counter, defaultdict


def p95(values: list[float]) -> float:
    """p95 theo nearest-rank: sắp xếp, lấy phần tử thứ ceil(0.95 * n)."""
    ordered = sorted(values)
    rank = (95 * len(ordered) + 99) // 100  # ceil(0.95 * n) bằng số nguyên
    return ordered[rank - 1]


def analyse(pairs: list[tuple[str, float]]) -> dict:
    counts = Counter()
    latencies = defaultdict(list)
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95_by_route = {route: p95(vals) for route, vals in latencies.items()}
    slowest = max(p95_by_route, key=p95_by_route.get) if p95_by_route else None

    return {"counts": counts, "p95": p95_by_route, "slowest": slowest}


if __name__ == "__main__":
    result = analyse([("/a", 10), ("/a", 20), ("/b", 5)])
    assert result["counts"] == Counter({"/a": 2, "/b": 1})
    assert result["p95"] == {"/a": 20, "/b": 5}
    assert result["slowest"] == "/a"

    # 1..20 -> phần tử thứ 19; 1..100 -> phần tử thứ 95
    assert analyse([("/x", i) for i in range(1, 21)])["p95"] == {"/x": 19}
    assert analyse([("/x", i) for i in range(1, 101)])["p95"] == {"/x": 95}

    # thứ tự đầu vào không ảnh hưởng
    assert analyse([("/x", 30), ("/x", 10), ("/x", 20)])["p95"] == {"/x": 30}

    # danh sách rỗng
    empty = analyse([])
    assert empty["counts"] == Counter()
    assert empty["p95"] == {}
    assert empty["slowest"] is None

    print("all ok")