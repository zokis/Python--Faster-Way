class Spam():
    def __init__(self):
        self.eggs = 'eggs'


def a():
    spam = Spam()
    if hasattr(spam, 'eggs'):
        eggs = spam.eggs
    else:
        eggs = None
    return eggs
