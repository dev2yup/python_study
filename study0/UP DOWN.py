print("""업다운 게임 룰
============================================================
0 ~ 150 까지의 숫자가 무작위로 설정됩니다.
설정된 숫자보다 입력값이 작으면 "UP"이 출력됩니다.
설정된 숫자보다 입력값이 크면 "DOWN"이 출력됩니다.
설정된 숫자와 입력값이 같으면 승리입니다.
시도한 횟수가 출력됩니다.
============================================================""")

from random import *

rand_num = randint(0, 150) # 0 ~ 150까지의 랜덤 정수 설정
count = 0 #시도 횟수



while True:
    
    input_num = int(input("0 ~ 150 사이의 숫자를 입력하세요. :  "))
    
    if input_num == rand_num: # 정답일 경우
        count += 1
        print("정답입니다!!")
        print("%s번 만에 성공하셨습니다!" %count)
        restart = input("재시작 하시겠습니까?(예, 아니오): ") # 게임 재시작 여부
        if restart == "예":
            rand_num = randint(0, 150) # 설정값 리셋
            count = 0
        else:
            print("게임을 종료합니다.") # 프로그램 종료
            break
    
    elif input_num > rand_num: # 입력값이 설정값보다 클 경우
        count += 1
        print("DOWN")
   
    elif input_num < rand_num: # 입력값이 설정값보다 작을 경우
        count += 1
        print("UP")


