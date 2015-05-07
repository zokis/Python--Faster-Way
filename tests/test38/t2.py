class Spam():
    def __init__(self):
        self.eggs = 'eggs'


def a():
    spam = Spam()
    try:
        eggs = spam.eggs
    except AttributeError:
        eggs = None
    return eggs
