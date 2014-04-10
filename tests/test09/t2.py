def a():
    a = [1, 2, 3, 4, 5]
    s = 0
    for i in range(len(a)):
        s += i
        s += a[i]
    return s
