inFp=None
fName, inList, inStr="", [], ""

# fName=input('파일명을 입력하세요')
fName="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"
inFp=open(fName, "r", encoding='utf-8')

inList=inFp.readlines() #list에 담음
# print(inList)

for inStr in inList:
    print(inStr, end="")

inFp.close()
