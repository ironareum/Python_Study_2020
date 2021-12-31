# for i in range(2, 9):
#     print('%d 단' %i)
#     for j in range(2, 9):
#         print('%d x %d = %d' %(i, j, i*j))
for i in range(2,10):
    print('# %d 단 #' %i , end=" ")
print()
for i in range(1, 10):
    for j in range(2, 10):
        print('%d x %d = %d' %(j, i, i*j), end=" ")
    print()
