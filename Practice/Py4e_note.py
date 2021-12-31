## 변수, 표현식, 문장

# 상수(constants)
# 값이 변하지 않음
print(123)
print(98.6)
print('hello')

# 예약어(reserved words)
# 예약어 종료 확인 https://www.programiz.com/python-programming/keyword-list

# 변수(variables)
# x, y: 메모리에 할당된 변수의 이름
# =: 할당자이며 해당 변수에 특정값을 넣어주는 역할 (<-)
 x = 12.2
 print(x)

## 연산자

# type()
# 값이나 변수의 타입을 알고 싶을때
a = 'hello' + 'world'
print(a)   # hello world
type(a)    # class 'str' 문자열
type(1)    # class 'int' 정수
(type(1.0)  # class 'float' 부동 소수점

# 타입변환
# str, int, float
i = 42
type(i) # int타입
f = float(i)    # float타입으로 변환
print(f)    # 42.0 출력
type(f) # float 타입

# 입력
# input()
name = input('What is your name?  ')
print('Welcome',name)

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
grosspay = float(hours) * float(rate)
print('Pay:', grosspay) # grosspay

# 연산자의 종류와 순서
# https://www.programiz.com/python-programming/operators


## 조건문

# if()
x = 5
if x <10 :
    print('smaller')

# if else
# 첫번째 조건문의 조건이 거짓인 경우에 대해 처리하기 위해 else 사용
x = 11
if x <10 :
    print('smaller')    # false
else :
    print('bigger') # 출력


# elif (다중분기 Multi-way decisions)
# 하나의 조건문 블럭에 필요한 조건문들을 추가할 수 있음
x = 30
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
elif x < 20 :
    print('Big')
elif x < 40 :       #Large가 출력됨
    print('Large')
else :              #elif에 해당값이 없을때 else가 없으면?
    print('large')
print('All done')


# try / except
# 파이썬에서 발생할 수 있는 error에 대해 프로그래머가 미리 대처할 수 있음
 a = '123'
try :
     print('hello') #출력
     b = int(a)
     print('world') #출력
except :
    b = 'integer로 변환할 수 없습니다'
print('done', b)    #출력
# 입력값이 잘못되었을 경우 프로그램이 종료되고 멈출것(error)이 아니라, 올바른 입력값을 넣도록 하는것이 합리적인 방법임


### py4e 3.1 test
# over 40 hours, gets 1.5 rates

hour = input('Enter Hours: ')
rate = input('Enter Rate: ')
hr = float(hour)
rt = float(rate)

reg = hr * rt
over = (hr - 40) * (rt * 0.5)

if hr > 40 :
    # print('overtime')
    final = reg + over
else :
    # print('regular')
    final = reg

print('Pay:', final)

### py4e 3.2 test
# if enter str, print 'error'

hour = input('Enter Hours: ')
rate = input('Enter Rate: ')

try :
    hr = float(hour)
    rt = float(rate)

    reg = hr * rt
    over = (hr - 40) * (rt * 0.5)

    if hr > 40 :
        # print('overtime')
        final = reg + over
    else :
        # print('regular')
        final = reg
    print('Pay', final)
except :
    print('Error, please enter numeric input')

### py4e 3.3 test
# score btw 0.0 and 1.0
# if score is out of range, print an 'error'
# if score is btw a grade using the following table

score = input('Enter Score: ')
x = float(score)
try :
    if x >= 0.9 :
        print('A')
    elif x >= 0.8 :
        print('B')
    elif x >= 0.7 :
        print('C')
    elif x >= 0.6 :
        print('D')
    elif x < 0.6 :
        print('F')
except :
    print('Error, the value out of range')



## 함수 (function)
# def:
# 반복되는 코드의 묶음 (예약어)
def greeting() :
    print('Hello') #여기선 hello가 인자

greeting()  # Hello 출력

# 인자 (= factor = argument)
# 함수를 호출할때 전달하는 값
# ex) print 함수()안에 들어가는 문자열 = 인자

# 매개변수(parameters)
# 함수가 정의된 곳에서 변수(variables)처럼 사용하는 것
def greet(lang) :
    if lang == 'es' :   # lang이 매개변수
        print ('hola')
    elif lang == 'fr' :
        print ('bonjour')
    else :
        print ('hello')
greet('en') # hello 출력

# 반환값 (return value)
# 인자를 받아 계산하고 함수 호출 구문이 사용할 수 있도록 값을 반환
def greet() :
    return 'hello'
print (greet, 'Areum')  # hello Areum 출력
# fruitful 함수는 결과(또는 반환값)을 생성 ??

# 다중매개변수 / 인자
# 함수 정의에서 한 개 이상의 매개변수를 정의할 수 있음
def add(left, right) :
    return left + right
print(add(1,2))  # 3 출력

def add(a,b) :
    added = a + b
    return added
x = add(3, 5)
print(x)    # 8 출력


### py4e 4.6 test
# use function name as 'computepay' and parameters as 'hours' and 'rate'
# enter hour : 45 / enter rate : 10 / pay 475.0
def computepay(hours, rate) :
    # print ('In computepay', hour, rate)

    reg = hr * rt
    over = (hr - 40) * (rt * 0.5)

    if hr > 40 :
        final = reg + over
    else :
        final = reg
    # print('returning', final)
    return final

hour = input('Enter Hours: ')
rates = input('Enter Rate: ')
hr = float(hour)
rt = float(rates)

p = computepay (hr, rt)
print('Pay:', p)


# function called 'Computepay()'
# 45 hours / rate 10.50
# rate 1.5 times over 40 Hours
# use input / float()

def computepay(h, r) :
    #print('computepay', a, b)

    reg = hr * rt
    over = (hr - 40) * (rt * 0.5)

    if hr > 40 :
        final = reg + over
    else :
        final = reg
    return final

hours = input('enter hours: ')
rate = input('enter rate: ')
hr = float(hours)
rt = float(rate)

p = computepay (hr, rt)
print(p)



# 번복문
# while:
# 무한루프에 빠질수 있는 단점이 있음. 코드를 되돌아볼 필요가 있음

# 반복(루프) 끝내기 / 종료
# break
# 루프를 종료하고 while문 바로 뒤의 코드를 실행
while True :
    linee = input('write something: ' )
    if linee == 'done' :
        break   # 루프 끝내기
    print (linee)
print('Done!')

# continue
# 현재 반복을 끝내고 루프의 시작으로 점프해서 다음 반복을 실행
while True :
    line = input('type something: ')
    if line[0] == '#':
        continue
    elif line == 'done' :
        break
    print(line)
print('done')

# 유한 루프 (definite loop)
# for () in:
for i in (5,4,3,2,1):
    print(i)
print('done')

# 문자열 이용
friends = ('M', 'A', 'S')
for friend in friends :
    print ('Hi', friend)

# 루프의 응용
# 최대값 찾기
largest_so_far = -1
print('Before', largest_so_far)
number = (9, 41, 12, 3, 74, 15)
for the_num in number :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print('largest_so_far: ',largest_so_far, 'the_num: ', the_num)
print('After', largest_so_far)

# 카운팅 하기
zork = 0
print('Before', zork)
for thing in (9, 41, 12, 3, 72, 15) :
    zork = zork +1
    print(zork, thing)
print('After', zork)

#  Sum 구하기
zork = 0
print('Before', zork)
for thing in (9,41, 12, 3, 74, 15) :
    zork = zork + thing
    print (zork, thing)
print('After', zork)

# 평균값 구하기
count = 0
sum = 0
print('Before', count, sum)
for value in (9,41, 12, 3, 74, 15) :
    count = count + 1
    sum = sum + value
    print (count, sum, value)
print('After', count, sum, sum/count)

# 필터링 하기
print('Before')
for value in (9,41, 12, 3, 74, 15) :
    if value >20 :
        print ('Large number', value)
print('After')

# Boolean ????
# 단순탐색으로 어떤값이 존재하는지 알고싶다면, False값으로 시작하는 변수를 도입해서 찾고자 하는 값을 찾는순간 값을 True로 바꿈
found = 'False'
print('Before', found)
for value in (9,41, 12, 3, 74, 15) :
    if value == 3 :
        found = 'True'
        break
    print (found, value)
print('After', found, value)

# 최소값 구하기
smallest_so_far = 100
print('Before', smallest_so_far)
number = (9, 41, 12, 3, 74, 15)
for the_num in number :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print('smallest_so_far: ',smallest_so_far, 'the_num: ', the_num)
print('After', smallest_so_far)

# None 타입
# 최소, 최대값을 구하는 좋은 테크닉 "None"사용하기
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# is 와 is not 연산자
