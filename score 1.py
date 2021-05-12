index = 50

from random import *
a = []

while index >= 1:
    b = randint(0, 100)
    a.append(b)
    index -= 1
    if index == 0:
        print(a)
        print((len(a)))

grade = []

for m in a:
    if m >= 90:
        grade.append("A")
    elif m >= 80:
        grade.append("B")
    elif m >= 70:
        grade.append("C")
    elif m >= 60:
        grade.append("D")
    elif m >= 50:
        grade.append("E")
    else:
        grade.append("F")

print(grade)

countA = 0
countB = 0
countC = 0
countD = 0
countE = 0
countF = 0

for n in grade:
    if n == "A":
        countA += 1
    if n == "B":
        countB += 1
    if n == "C":
        countC += 1
    if n == "D":
        countD += 1
    if n == "E":
        countE += 1
    if n == "F":
        countF += 1

print(countA, countB, countC, countD, countE, countF)