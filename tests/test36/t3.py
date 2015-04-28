def a():
    r = []
    for x in range(5):
        _r = []
        for y in range(5):
            _r.append(0)
        r.append(_r)
    return r
