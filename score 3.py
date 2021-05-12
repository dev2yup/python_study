countA = 0
countB = 0
grade = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D']

for n in grade:
    if n == 'A':
        countA += 1
    elif n == 'B':
        countB += 1

print(countA)
print(countB)

a = [91, 70, 80, 55, 67]
c = []

for m in a:
    if m >= 90:
        c.append("A")

print(c)