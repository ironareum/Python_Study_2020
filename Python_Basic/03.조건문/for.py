i, hap =0,0

for i in range(501, 1001, 2):
  hap+=i
print(hap)


# 1부터 입력한 값까지의 합 구하기
sum=0
# num = int(input('값 입력:'))
num=100
for i in range(1, num+1, 1):
    sum+=i
print(sum)

# 구구단 몇단?
i, dan =0,0
# dan = int(input('몇단? : '))
dan = 5

for i in range(1, 10, 1):
    print('%d x %d = %d' %(dan, i, dan*i))
