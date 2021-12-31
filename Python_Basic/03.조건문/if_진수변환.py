# -*- coding: utf-8 -*-
from platform import python_version
print(python_version())
import sys
import io
#한글깨짐
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#진수 변환 프로그램 완성
sel = int(input("입력진수 결정(16/10/8/2) : "))
# int(input("입력진수 결정(16/10/8/2) : "))
num = input("값 입력 : ") #10진수 값 입력 #!!!! python3에서는 입력값 항상 문자형으로 받음. python2에서는 자동 형변환 해줌............ ㅠㅠ
# print(type(num)) #여기서 num은 스트링형.
if sel == 16:
    num10= int(num, 16) #16진수 -> 10진수 변환.
    print("num10 = 10 진수: ",num10)
    print("hex code: ",hex(num10))
elif sel == 10:
    num10= int(num, 10)
elif sel == 8:
    num10= int(num, 8)
elif sel == 2:
    num10= int(num, 2)

print("16진수 :", hex(num10))
print("10진수 :", num10)
print("8진수 :", oct(num10))
print("2진수 :", bin (num10))
