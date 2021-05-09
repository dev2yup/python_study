score = int(input("점수 입력:"))
if score>100 or score<0:
    print("""잘못된 점수입니다.
프로그램을 종료합니다.""")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("E")
else:
    print("F")

print("성적처리 완료.")
