from random import *

total = int(input("학생 수를 입력하세요."))
alpha = total
rand = randint(1, 100)

a = []
while alpha >= 1:
    rand = randint(1, 100)
    a.append(rand)
    alpha -= 1
    if alpha == 0:
        print(a)

b = []

for m in a:
    if m >= 90:
        b.append("A")
    elif m >= 80:
        b.append("B")
    elif m >= 70:
       b.append("C")
    elif m >= 60:
        b.append("D")
    elif m >= 50:
       b.append("E")    
    else:
       b.append("F")
       
print(b)
print("(A)맞은 학생 수:", b.count("A")); 
print("(B)맞은 학생 수:", b.count("B")); 
print("(C)맞은 학생 수:", b.count("C"));
print("(D)맞은 학생 수:", b.count("D")); 
print("(E)맞은 학생 수:", b.count("E"));
print("(F)맞은 학생 수:", b.count("F"));

print("(A) 학생의 비율: {}%".format(int(b.count("A")/total*100)))
print("(B) 학생의 비율: {}%".format(int(b.count("B")/total*100)))
print("(C) 학생의 비율: {}%".format(int(b.count("C")/total*100)))
print("(D) 학생의 비율: {}%".format(int(b.count("D")/total*100)))
print("(E) 학생의 비율: {}%".format(int(b.count("E")/total*100)))
print("(F) 학생의 비율: {}%".format(int(b.count("F")/total*100)))
