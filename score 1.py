total = int(input("전체 학생 수를 입력해 주세요."))
index = total

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

print("A를 받은 사람: ", int(countA), "명", sep="")
print("B를 받은 사람: ", int(countB), "명", sep="")
print("C를 받은 사람: ", int(countC), "명", sep="")
print("D를 받은 사람: ", int(countD), "명", sep="")
print("E를 받은 사람: ", int(countE), "명", sep="")
print("F를 받은 사람: ", int(countF), "명", sep="")

print("A를 받은 사람 비율: " , int(countA/total*100) , "%", sep="")
print("B를 받은 사람 비율: " , int(countB/total*100) , "%", sep="")
print("C를 받은 사람 비율: " , int(countC/total*100) , "%", sep="")
print("D를 받은 사람 비율: " , int(countD/total*100) , "%", sep="")
print("E를 받은 사람 비율: " , int(countE/total*100) , "%", sep="")
print("F를 받은 사람 비율: " , int(countF/total*100) , "%", sep="")

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
grade2 = ['A', 'B', 'C', 'D', 'E', 'F']
values = [countA, countB, countC, countD, countE, countF]

plt.bar(x, values, width = 0.5, color = "green")
plt.xticks(x, grade2)
plt.show()
       