#eval
#range

sel = int(input('1.수식계산기 2.두수 사이 합계 : '))

if sel==1:
    sic = input('***수식을 입력하세요')
    answer = eval(sic) #eval
    print('%s 결과는 %5.1f 입니다.' %(sic, answer))

elif sel==2:
    num1 = int(input('***첫번째 숫자를 입력하세요'))
    num2 = int(input('***두번째 숫자를 입력하세요'))
    temp = num1
    for temp in range(num1, num2): #range
        result=+temp
    print('%d +...+ %d는 %d 입니다.' %(num1, num2, result))
else:
    print('1 또는 2만 입력해야 합니다.')
