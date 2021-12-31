# money =int(input("교환할 돈은 얼마?"))
money = 7777

c500, c100, c50, c10 = 500, 100, 50, 10
to500, to100, to50, to10 = 0,0,0,0

to500 = money//c500
money %= c500 #500원으로 나눈 나머지

to100 = money//c100
money %= c100 #100원으로 나눈 나머지

to50 = money//c50
money %=c50

to10 = money//c10
money %= c10


print('오백원짜리', '%d 개' %to500 )
print('백원짜리', '%d 개' %to100)
print('오십원짜리', '%d 개' %to50)
print('십원짜리', '%d 개' %to10)
print('바꾸지못한 잔돈', '%d 개' %money)

print('총합', to500*500 + to100*100 + to50*50 + to10*10 + money)
