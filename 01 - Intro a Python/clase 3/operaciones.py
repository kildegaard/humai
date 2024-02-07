def factor(n: int) -> int:
    res = n if n != 0 else 1
    while n > 1:
        n -= 1
        res *= n
    return res
