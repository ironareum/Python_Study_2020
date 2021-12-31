import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)
sys.stdin.encoding


# 제곱 연산자
a=100**100 #100의 100제곱
print(a)

a=10; b=20
print(a+b, a-b, a*b, a/b, a%b)

#나눈후 소수점을 버리는 //
a,b =9,2
print(a%b ,a/b, a//b)

#boolean
a=True
print(type(a))

a=(100==100)
b=(100<10)
print(a,b)

#스트링
a='파이썬 만세'
a
print(a)
print(type(a))

b='''파이썬
만세'''
print(b)


#산술 연산자 순서
a,b,c = 2,3,4
print(a+b-c, a+b*c, a*b/c) #1,14,1.5

#문자열과 숫자의 상호 변환
s1, s2, s3 ="100", "100.123", "999999999"
print(int(s1)+1, float(s2)+1, int(s3)+1 )

#숫자를 문자열로
a=100; b=100.123
print(str(a)+'1', str(b)+'1')
a_=str(a)+'1'; b_=str(b)+'1'
print(a_,b_)
