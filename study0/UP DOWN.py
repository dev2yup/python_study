print("""업다운 게임 룰
============================================================
0 ~ 150 까지의 숫자가 무작위로 설정됩니다.
설정된 숫자보다 입력값이 작으면 "UP"이 출력됩니다.
설정된 숫자보다 입력값이 크면 "DOWN"이 출력됩니다.
설정된 숫자와 입력값이 같으면 승리입니다.
시도한 횟수가 출력됩니다.
============================================================""")

from random import *

rand_num = randint(0, 150)
count = 0



while True:
    
    input_num = int(input("0 ~ 150 사이의 숫자를 입력하세요. :  "))
    
    if input_num == rand_num:
        count += 1
        print("정답입니다!!")
        print("%s번 만에 성공하셨습니다!" %count)
        restart = input("재시작 하시겠습니까?(예, 아니오): ")
        if restart == "예":
            rand_num = randint(0, 150)
            count = 0
        else:
            print("게임을 종료합니다.")
            break
    
    elif input_num > rand_num:
        count += 1
        print("DOWN")
   
    elif input_num < rand_num:
        count += 1
        print("UP")


