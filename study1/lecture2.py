from random import randint

total = int(input("학생 수를 입력하세요."))

alpha = total

rand = randint(1, 100)

a = []
while total >= 1:
    rand = randint(1, 100)
    a.append(rand)
    total -= 1
    if total == 0:
        print(a)

b = []

for m in a:
    if m >= 90:
        b.append("A")
    elif m >= 80:
        b.append("B")
    elif m >= 70:
       b.append("C")
    else:
       b.append("D")
    print(b)
    
    
    



