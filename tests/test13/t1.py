def a():
    a = 1
    b = 2
    c = 2
    d = 5
    return (a.__add__(b.__add__(c))).__mul__(d)
