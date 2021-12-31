import random

def lotto():
    return random.randrange(1,46)

print('로또 추첨을 시작합니다.')
nums=[]

#로또 번호 뽑기 ======
while True:
    # nums 리스트의 값 개수가 6 미만일때
    if len(nums)>=6:
        break
    #nums에 동일한 값 있는지 여부 확인
    num = lotto()
    if nums.count(num)==0:
        nums.append(num)

# print(nums)
nums.sort() #sort()실행후 값을 어디 변수에 담는게 아님.. 주의!
print(nums)
print('추첨된 로또 번호 ===> ' , end='')
for i in range(0,6):
    print('%d ' %nums[i], end='')
