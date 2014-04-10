def a(n=25):
    a, b = 0, 1
    for i in range(n):
        x = a + b
        a = b
        b = x
    return a
