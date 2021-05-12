from random import *

for i in range(100):
    randint(0, 100)

score = randint(0, 100)
print(score)

#score = int(input("점수 입력:"))
if score>100 or score<0:
    print("""잘못된 점수입니다.
프로그램을 종료.""")

elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
elif score>=50:
    print("E")
else:
    print("F")

print("성적처리 완료.")
