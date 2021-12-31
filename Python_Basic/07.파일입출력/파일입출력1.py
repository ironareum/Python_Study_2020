inFp=None #입력파일
inStr='' #읽어온 문자열

path="/Users/areumkangair/Documents/Work_Python/test/fileIO/미나리.txt"
inFp = open(path, 'r', encoding='utf-8') #파일 오픈

inStr = inFp.readline() #한줄씩 읽기 (읽고나면 커서가 젤 뒤로 이동...? )
print(inStr, end='')#젤 뒤로간 커서가 '\n'을 읽었기 때문에 줄이 2번 내려감 

inStr = inFp.readline()
print(inStr, end='')

inStr = inFp.readline()
print(inStr, end='')
