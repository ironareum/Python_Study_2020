aa =[]
bb =[]
val=0
for i in range(0, 101):
    aa.append(val)
    val+=2

for i in range(0,101):
    bb.append(aa[100-i])

print(aa)
print(bb)

a=[10,20,30]
a[1:2] =[100,200]
print(a)

a=[10,20,30]
a[1] =[100,200]
print(a)
