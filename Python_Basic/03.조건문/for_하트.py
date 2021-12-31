# nums = int(input('숫자를 여러개 입력하세요.'))
nums = "5411260745"

size = len(nums)
print(size)
print(type(size))
for line in range(0,size,1):
    num=int(nums[line])
    mark='*'
    print(mark*num)
