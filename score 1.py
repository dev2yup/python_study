index = 50

from random import *
a = []

while index >= 1:
    b = randint(0, 100)
    a.append(b)
    print(a)
    index -= 1
    if index == 0:
        print((len(a)))