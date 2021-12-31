
from platform import python_version
import sys

#파이썬 버전 체크 : 스크립트 환경설정에서 파이썬2->파이썬 3으로 바꿔줘야함
print(python_version())

#출력하기
print('#출력하기======')
print("hello")

#한칸씩 띄워쓰기
print('\n#한칸씩 띄워쓰기======')
print("h", "e","l","l","o")

#구분자 주기
print('010','1234','5678', sep='-')

#자동 줄바꿈 없이 붙여쓰기
print('hello', end=' ')
print('world', end='')
print()
# ???????????
print('Learn python', file=sys.stdout)
#print('error messege: ?!?! ', file=sys.stderr) #에러 빨간색 글씨?? 안되는데??
# print('Learn python', file='test.txt')

# format 사용법
print('%s' %1)
print('%d' %1)
print('%s' %('one'), '%d' %1)
print('{1} {0}'.format('one', 'two'))

#글자에 공백주기
print('%10s' %('love')) #10자리에서 오른쪽부터 채우고 나머지 공백
print('{:>10}'.format('love'),'#오른쪽부터 10자리') #오른쪽부터 채우고 나머지 공백
print('{:10}'.format('love'),'#오른쪽부터 10자리') #오른쪽부터 채우고 나머지 공백
print('{:<10}'.format('love'),'#왼쪽부터 10자리') #왼쪽부터 채우고 나머지 공백
print('{}'.format('3'))
print("{:>5}".format('cat'))
print('%-10s' %('happy'), '#왼쪽부터 10자리')
print('{:10}'.format('happy'), '#왼쪽부터 10자리')

#공백대신 다른 문자로 채우기
print('{:_>10}'.format('hello'))
print('{:*>10}'.format('hello'))

#중앙정렬
print('{:^10}'.format('hello'))

#.붙이기 = 절삭
print('%.8s' %('happyland')) #8자리 공간 확보 후 절삭
print('%.5s' %('happyland')) #8자리 공간 확보 후 절삭
print('%.3s' %('happyland')) #8자리 공간 확보 후 절삭

#n자리까지 문자 절삭 후 공백확보
print('{:10.5}'.format('minionslove'), '공백확보')

# %d 활용 (d:정수)
print('%d %d' %(1,2)) #int type
print('{}{}'.format('1', '2')) #string type
print('%d' %(42))
print('{:4d}'.format(42)) #총 4자리수 확보 -> 왼쪽공백

# %f 활용 (f:실수)
print('%f' %(3.1415)) #기본 소수점 뒤 6자리
print('{}'.format(3.1415324225))
print('{:f}'.format(3.1415324225))
print('%f' %(3.1415324225)) #기본 소수점 뒤 6자리
print('%1.8f' %(3.1415324225))#쩜 앞에는 정수부, 뒤에는 소수부 자리 제어
print('%08.2f' %(3.1415324225)) #총 8자리중 소수점은 뒤에 2자리, 빈공간은 0으로 채
print('{:08.2f}'.format(3.1415324225))

#예제
print('%d / %d = %5.1f' %(100,200,0.5))
print('%5f' %123.45)
print('%7.1f' %123.45)
print('{0:d} {1:5d} {2:05}'.format(123, 123, 123))

print('새로운\t문자\b\'\n새로운문자\'')
print('\\\\\\역슬래쉬 세개 출력')
print(r'\n \t \" \\를 그대로 출력') #r 붙이면 그대로 출력
print('줄바꿈 \n 줄바꿈')
print('줄바꿈 \ 줄바꿈')
print(r'줄바꿈 \n 줄바꿈')
print ("1"),
print ("2")


#2진수 입력-> 10진수 출력 (0b 붙이기)
print(0b10010011) #10진수로 출력
print(int('10010011', 2))

#16진수 입력 -> 10진수 출력 (0x)
print(0x93)
print(int("93", 16))

#2진수로 출력하기
print(bin(13))
print(bin(0x13)) #16진수
print(bin(0xC5F7)) #16진수
print(hex(13))
