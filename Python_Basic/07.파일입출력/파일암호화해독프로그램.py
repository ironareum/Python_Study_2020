inFp, outFp="",""
encNum=0
# sel=input('1.암호화  2.암호해석 중 선택 : ')
# inFname=input('읽을 파일명을 입력하세요 : ')
# outFname=input('저장할 파일명을 입력하세요 : ')
sel="1"

#암호화 파일 ==========
# inFname="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"
# outFname="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리암호화1.txt"
#복호화 파일 ==========
inFname="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리암호화.txt"
outFname="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리암호해독.txt"



if sel =="1":
    encNum=100
elif sel =="2":
    encNum=-100
else :
    print('번호선택을 잘못 했어요')

if inFname!="":
    inFp=open(inFname, "r", encoding="utf-8")
    outFp=open(outFname, "w", encoding="utf-8")

#방법1)내방법 ======================
inList=inFp.readlines() #한번에 다불러옴

newList=""
line=""
for inStr in inList:
    for char in inStr:
        if char!="":
            line+=chr(ord(char)+encNum)
        else :
            line+=char

outFp.writelines(line)
print(line)
#0.08s

#방법2)교안방법=======================
# while True:
#     inList=inFp.readline()
#     if not inList:
#         print("불러올 내용 없음")
#         break
#
#     newList=""
#     line=""
#
#     for i in range(0, len(inList)):
#         ch=inList[i]
#         print('ch: %s' %ch)
#         newCh=ord(ch)+encNum
#         line+=chr(newCh)
#
#     outFp.writelines(line)
#     print(line)
    #0.09s
inFp.close()
outFp.close()
