#파일입출력 ======
#입력함수:  read(), readline(), readlines()
#출력함수: write(), writelines()
# sel=int(input('1.암호화 2.암호해석 중 선택: '))
sel="1"

readFileName=input('입력 파일명을 입력하세요 : ')
saveFileName=input('출력 파일명을 입력하세요 : ')


path="/Users/areumkangair/Documents/Work_Python/test/fileIO"
fileOpen=io.open('readFileName', 'wb')
# fileOpen=io.open('readFileName', 'wb')
fileOpen.write('path','saveFileName')

print('%s ---> %s 변환완료')
