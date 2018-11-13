#!/usr/bin/env python3

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):  # the __repr__ method returns the code representation of an instance, and is usually text you type to re-create the instance
        return 'Pair({0.x!r}), {0.y!r}'.format(self)
    def __str__(self): # the __str__ method converts the instance to a string, and is the output produced by the str() and print() functions
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))
