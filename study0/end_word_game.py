print("끝말잇기 게임을 시작합니다.\n각각의 사용자에게는 2번의 기회가 주어집니다.")
print("10초가 지나도록 답을 하지 못하거나 답이 틀린다면 기회 하나를 잃습니다.")
print("2번의 기회를 먼저 잃는 사람이 패배하게 됩니다.")
print('게임을 중단 하고 싶으시면 첫 단어 이후  "중지" 를 입력해주세요.\n===================================================')

user1 = input("사용자1의 이름을 입력하세요. ")
user2 = input("사용자2의 이름을 입력하세요. ")
count1 = 2 #사용자1 의 기회 수
count2 = 2 #사용자2 의 기회 수
win1 = 0 #사용자1의 승리 수         
win2 = 0 #사용자2으 승리 수

if True:

    import time #시간 모듈(입력하기까지 지난 시간 기록)
    start_time = time.time()
    input_str1 = input("첫 단어를 입력하세요.") #첫 단어 입력
    timer = 0
    timer = time.time() - start_time

    if timer > 10: #10초 초과 일 때 
        
        print("시간 초과입니다.")
        print(timer, "초")
        count1 -= 1
        print("%s님의 기회는 %d번 남았습니다." %(user1, count1))
 
    elif len(input_str1) < 2:

        input_str1 = input("2글자 이상의 단어를 입력해 주세요.")
        

last_str = input_str1[-1]

while True:

    import time 
    start_time = time.time()
    timer = 0
    input_str2 = input("%s님, '%s' 로 시작하는 단어를 입력하세요. " %(user2, last_str)) #사용자2 입력
    timer= time.time() - start_time

 
    if input_str2 == "중지": #중지 입력 시 게임 종료

        print("[게임 종료]")
        break

    
    if timer > 10:

        print("시간 초과입니다.")
        print(timer, "초")
        count2 -= 1
        print("%s님의 기회는 %s번 남았습니다." %(user2, count2))

        if count2 == 0:

            win1 += 1 #승리 횟수 기록
            print(user1, "님이 승리 하셨습니다.")
            print("%s 님이 %d번 승리하였고, %s 님이 %d번 승리하였습니다." %(user1, win1, user2, win2)) #승리 횟수 출력
            count1 = 2
            count2 = 2

            

    elif input_str2[0] != last_str:

        count2 -= 1
        print("틀렸습니다. %s님의 기회는 %s번 남았습니다." %(user2, count2)) 
        if count2 == 0: 
            win1 += 1
            print(user1, "님이 승리 하셨습니다.")
            print("%s 님이 %d번 승리하였고, %s 님이 %d번 승리하였습니다." %(user1, win1, user2, win2))
            count1 = 2
            count2 = 2

    

    elif input_str2[0] == last_str:

        last_str = input_str2[-1]
        print(input_str2)

        if len(input_str2) < 2:
            reinput_str2 = input("두 글자 이상의 단어를 입력하세요. ")
            input_str2 = reinput_str2
            last_str = input_str2[-1]


    start_time = time.time() #사용자1 입력
    timer = 0
    input_str1 = input("%s님, '%s' 로 시작하는 단어를 입력하세요. " %(user1, last_str))
    timer= time.time() - start_time

    if input_str1 == "중지":
        print("[게임 종료]")
        break

    
    if timer > 10:

        print("시간 초과입니다.")
        count1 -= 1
        print(timer,"초")
        print("%s님의 기회는 %s번 남았습니다." %(user1, count1))
        print(timer,"초")

        if count1 == 0:

            win2 += 1
            print(user2, "님이 승리 하셨습니다.")
            print("%s 님이 %d번 승리하였고, %s 님이 %d번 승리하였습니다." %(user1, win1, user2, win2))
            count1 = 2
            count2 = 2


    elif input_str1[0] != last_str:

        count1 -= 1
        print("틀렸습니다. %s님의 기회는 %s번 남았습니다." %(user1, count1)) 

        if count1 == 0:

            win2 += 1
            print(user2, "님이 승리 하셨습니다.")
            print("%s 님이 %d번 승리하였고, %s 님이 %d번 승리하였습니다." %(user1, win1, user2, win2))
            count1 = 2
            count2 = 2

    elif input_str1[0] == last_str:

        last_str = input_str1[-1]
        print(input_str1)

        if len(input_str1) < 2:
            continue

            reinput_str1 = input("두 글자 이상의 단어를 입력하세요. ")
            input_str1 = reinput_str1
            last_str = input_str1[-1]
            