# val = input('문자열을 입력하세요')
val = "즐거운 Python 프로그래밍 ~~"
count = len(val)
li=''
for i in range(1, count+1):
    # print(i)
    # print(val[count-i])
    li+= val[count-i]
print(li)
