def a():
    a = [1, 2, 3, 4, 5]
    s = 0
    for p, v in enumerate(a):
        s += p
        s += v
    return s
