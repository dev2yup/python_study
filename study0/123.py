# print("{0}은 {1}다 {2}".format(1, "바보", 5))

# print("%s는 %s다" % ("이상빈", "바보"))


# from random import *
# a = input()

# b = 0
# c = 0
# for m in a:
#     if m == 1:
#         b += 1
#     if m == 2:
#         c += 1

# print(b)
# print(c)


print("콜라 1000원, 사이다 900원" )
print("품절 시 자판기가 종료 됩니다.")
print("0원을 입력하면 자판기가 종료됩니다.")
drink = input("콜라와 사이다 중 하나를 선택하세요: ")
coke = 6
cider = 6

while True:
  if drink == "콜라":
    money = int(input("돈을 넣어 주세요."))
    if money == 1000:
      print("콜라 한 캔이 나왔습니다.")
      coke -= 1
      print("콜라는 %d캔 남았습니다." % coke)  
    elif money > 1000:
      print("거스름돈 %d원 을 주고 콜라 한 캔을 줍니다."%(money - 1000))
      coke -= 1
      print("콜라는 %d캔 남았습니다." % coke)
    elif money == 0:
      print("자판기 종료")
      break
    elif money < 1000:
      print("%d원 을 돌려주고 콜라를 주지 않습니다."% money)
    
    if coke == 0:
      print("콜라가 품절 되었습니다.")
      break
  
  
  if drink == "사이다":
    money = int(input("돈을 넣어 주세요."))
    if money == 900:
      print("사이다 한 캔이 나왔습니다.")
      cider -= 1
      print("사이다는 %d캔 남았습니다." % cider)
    elif money > 900:
      print("거스름돈 %d원 을 주고 사이다 한 캔을 줍니다."%(money - 900))
      cider -= 1
      print("사이다는 %d캔 남았습니다." % cider)
    elif money < 900:
      print("%d원 을 돌려주고 사이다를 주지 않습니다."% money)
    elif money == 0:
      print("자판기 종료")
      break
    if cider == 0:
      print("사이다가 품절 되었습니다.")
      break
