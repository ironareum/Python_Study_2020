import os

inFp=""
fName, inList, inStr="","", ""

# fName=input("파일명을 입력하세요.")
fName="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"

if os.path.exists(fName):
    inFp=open(fName, 'r', encoding='utf-8')

    inList=inFp.readlines()
    # print(inList)
    for inStr in inList:
        print(inStr, end='')

    inFp.close()
else:
    print('%s \n입력하신 파일이 존재하지 않습니다.' %fName)
