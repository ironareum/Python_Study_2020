# outFp=""
outStr=""

# fName=input("파일명을 입력하세요.")
fName="/Users/areumkangair/Documents/Work_Python/test/fileIO/hello.txt" #오픈할 파일명이 없으면 생성됨
outFp=open(fName, 'a', encoding='utf-8') #w으로 하면 덮어쓰기...위험.

while True:
    outStr=input('내용 입력 : ')
    if outStr != "": #입력한 내용이 있을시
        outFp.write(outStr+"\n")
    else: #입력한 내용이 없으면 종료
        break
outFp.close()
print('정상적으로 파일에 써졌음.')
