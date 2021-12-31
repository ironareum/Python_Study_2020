'''
ord() : 문자의 고유한 숫자를 알려줌
chr() : 숫자에 해당하는 문자를 알려줌
'''

txt='파'
num=ord(txt)
print(num)

txt=chr(num)
print(txt)

#암호화 하기위해 '파'의 숫자에 100을 더함
newNum=ord(txt)+100
print(newNum)
print(chr(newNum))
