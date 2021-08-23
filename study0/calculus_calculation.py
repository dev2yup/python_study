from sympy import *
import matplotlib.pyplot as plt
import numpy as np

a, b = 0, 6 #이곳에 범위를 입력해주세요.
m = max(a,b)
n = min(a,b)
x = symbols('x') #기호변수 선언
 
fx = input("함수를 입력하세요. : ")
fx = sympify(fx)
fb = fx.subs(x, m) #함수에 m대입
fa = fx.subs(x, n) #함수에 n대입
print(fb)
print(fa)
result = (fb - fa) / (b - a)
   
print("평균변화율:", result,"입니다.")

x = symbols('x') #x를 기호변수화
fprime = Derivative(fx, x).doit() #x에 대하여 미분
print("fx 의 도함수는:", fprime, "입니다.")
n = fprime.subs({x: 3}) # 이곳에 X좌표를 입력해주세요.
print("fx에서 x = 3 에서의 순간변화율(미분계수)는", n , "입니다.")


plot(fprime, (x, -10, 10, 1), ylim=(-10, 10), title = "Derivative graph") 