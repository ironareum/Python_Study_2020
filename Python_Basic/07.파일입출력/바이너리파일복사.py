inFp, outFp ="", ""

inFname ="/Users/areumkangair/Documents/Areum/Home_2021.xlsx"
outFname ="/Users/areumkangair/Documents/Areum/Home_2021_Copy22.xlsx"

inFp=open(inFname, "rb")
outFp=open(outFname, "wb")

#방법1)
# while True:
#     inStr=inFp.read()
#     if not inStr:
#         break
#     outFp.write(inStr)

#방법2)
inStr=inFp.readlines()
outFp.writelines(inStr)


inFp.close()
outFp.close()
print('복사완료.')
