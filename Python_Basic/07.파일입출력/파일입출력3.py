inFp=None #입력파일
inList=""
path="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"

inFp=open(path, 'r', encoding='utf-8') #파일 오픈

inList=inFp.readlines() #한줄씩 읽어서 리스트로 반환
# print(inList)


for i in inList:
    print(i, end='')

inFp.close()
