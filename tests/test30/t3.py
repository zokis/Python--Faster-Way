def a():
    f = lambda *args: args
    return f(*'ab')
