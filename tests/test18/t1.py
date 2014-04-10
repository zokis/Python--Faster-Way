def a():
    l = range(50, -20, -2)
    d = {}
    for p, v in enumerate(l):
        d.update({p: v})
    return d
