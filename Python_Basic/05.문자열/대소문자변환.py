# 풀어야됨

text = '즐거운 Python 프로그래밍 ~~ '
outStr =''
for i in range(0, len(text)):
    ch=text[i]
    #대문자로 모두 변환
    if (ord(ch) >= ord('a')) and (ord(ch)<= ord('z')):
        newStr = text[i].upper()
        print(newStr)
    else :
        newStr = ch
    outStr+=newStr
print(outStr)
