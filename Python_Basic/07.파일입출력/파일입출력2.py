inFp=None #입력파일
inStr='' #읽어온 문자열
path="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"

inFp=open(path, 'r', encoding='utf-8') #파일 읽기

# inStr=inFp.read() #전체내용을 다 읽어옴
# print(inStr)
#
while True:
    inStr=inFp.readline()
    if inStr=='':
        break
    print(inStr, end='')

inFp.close()
