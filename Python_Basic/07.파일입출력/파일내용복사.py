inFp, outFp, inStr ="","",""
# inList=""

fName="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"
cpfName="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리복사.txt"


inFp=open(fName, 'r', encoding='utf-8')
outFp=open(cpfName, "w", encoding="utf-8")

inList=inFp.readlines()
print(inList)

for line in inList:
    outFp.writelines("**")
    outFp.writelines(line) #writelines
inFp.close()
outFp.close()

print('정상적으로 복사 완료.')
