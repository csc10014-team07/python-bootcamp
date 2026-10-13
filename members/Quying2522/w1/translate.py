def fib(n: int) -> list[int]:
    """Return the Fibonacci numbers smaller than n.

    Difference from C++: Python can swap and update two values in one
    line with a, b = b, a + b. The right side is evaluated first, so no
    temporary variable is needed. In C++, write
    int t = a + b; a = b; b = t;
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print("fib(100) = ",fib(100))