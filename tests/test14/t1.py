class Z():

    def __init__(self, v):
        self.v = v

    def __mul__(self, o):
        return Z(self.v * o.v)

    def __add__(self, o):
        return Z(self.v + o.v)


def a():
    a = Z(5)
    b = Z(2)
    c = Z(3)
    return (b + c) * a
