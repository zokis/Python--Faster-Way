def a():
    a = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
    b = {k: v for x, k, v in a}
    return b
