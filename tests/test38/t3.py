class Spam():
    def __init__(self):
        self.not_eggs = 'eggs'


def a():
    spam = Spam()
    if hasattr(spam, 'eggs'):
        eggs = spam.eggs
    else:
        eggs = None
    return eggs
