# print(abs(-10)) # 10
# print(pow(4, 2)) #16 (제곱)
# print(round(3.14)) # 3
# print(round(4.6)) # 5

# from math import *
# print(floor(4.99)) #내림 4
# print(ceil(3.14)) #올림 4
# print(sqrt(16)) #제곱근 4

# from random import *
# print(random() * 10) # 0.0 ~ 10.0 미만의 랜덤 값
# print(int(random() * 10)) # 0 ~ 10 미만
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 랜덤 값
# print(randrange(1, 46)) # 1 ~ 46 미만의 랜덤 값
# print(randint(1, 45)) # 1 ~ 45 이하의 랜덤 값

# date =  (randint(4, 28))
# print("오프라인 모임 날짜는 매월" + str(date) + "일로 결정 되었습니다.")

# a = "12345"

# print(a[:2]) #처음부터 2 직전까지
# print(a[-4:]) #맨 뒤에서 부터 4까지

# python = "Python Is Amazing"
# print(len(python)) #문자열의 길이 
# print(python.replace("Python", "Java")) #단어 대체

# print("나는 %d살 입니다." % 20)
# print("나는 %s를 좋아해요." % "파이썬") #%d 정수 %s 문자열 %c 한글자
# print("나는 {}살 {} 입니다.".format(20, "이동엽"))

# a = ["김", "이", "박"]
# print(a.index("김")) #김은 몇번째인가(0부터 시작)
# a.append("최"); print(a) #끝에 최 추가
# a.insert(1, "정"); print(a) #1번에 정 추가
# print(a.pop()) #끝에 있는 사람 뺌
# print(a.count("김")) #김이 몇번 있는지
# #리스트 확장 리스트1.extend(리스트2) 둘이 합쳐짐

# a = {3 : "유재석", 100 : "김태호"}  
# print(a[100]) # 값 없을 때 오류 출력 후 종료
# print(a.get(3)) # 값 없을 때 None 출력후 진행
# print(a.get(5, "사용 가능")) #None 대신 사용 가능 출력
# print(3 in a) # True
# print(5 in a) #False
# a[4] = "조세호" #4에 조세호 입력
# del a[3] #3 삭제
# print(a.keys()) #키들만 출력
# print(a.values()) # values 들만 출력
# print(a.items()) #둘 다 출력
# a.clear() # 사전 삭제

#튜플 - 내용 변경, 추가X
# a = ("돈까스", "생선까스")
# name, age , hobby = "김종국", 20, "코딩"
# print(name, age, hobby)

#세트 - 중복 , 순서 X
# my_set = {1,2,2,3,3,3} #{1,2,3}

# java = {"김", "이", "박"}
# python = {"김", "최"} #set(["김", "최"])
# #교집합
# print(java & python)
# print(java.intersection(python))
# #합집합
# print(java | python) 
# print(java.union(python))
# #차집합
# print(java - python)
# print(java.difference(python))
# #세트에 추가 
# python.add("이")#하나만 추가 가능
# print(python)
# pkython.remove("최") #세트에서 제거
# print(python)

a = int(input())

print(-a)