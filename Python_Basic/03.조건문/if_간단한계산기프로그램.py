num1 = int(input('첫번째 수를 입력하세요 : '))
sign = input('계산할 연산자를 입력하세요 : ')
num2 = int(input('두번째 수를 입력하세요 : '))
result=0

if sign=='+':
    result=num1 + num2
elif sign=='-':
    result=num1 - num2
elif sign=='*':
    result=num1 * num2
elif sign=='/':
    result=num1 / num2
elif sign=='**':
    result=num1 ** num2
elif sign=='%':
    result=num1 % num2


print("%d %s %d = %f 입니다." %(num1, sign, num2, result))
