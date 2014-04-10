def a():
    a = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
    b = {x[1]: x[2] for x in a}
    return b
