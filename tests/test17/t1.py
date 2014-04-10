def a():
    d = {}
    for i in range(100):
        d.update({str(i): i*2})
    return d
