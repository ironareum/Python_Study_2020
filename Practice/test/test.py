import re
ipt = input("Enter name of the file: ")
if len(ipt) <=0:
  ipt = "regex_sum_42.txt"
hand = open(ipt)
hn = open(ipt)
count =[]
# WHY?????
numts = re.findall("[0-9]+",hn.read())
print("test:",numts )

# why not this??? .read() only read once???? ====> Yes.
# ==== USE seek(0)
hand.seek(0)
line = hand.read()
num = re.findall("([0-9]+)",line)
print("num: ",num)

# k=[int(i) for i in numts]
# print(k, type(k[0]))
hand.seek(0)
print(sum([int(i) for i in re.findall("[0-9]+", hand.read())]))

'''
for line in hand:
  line = line.rstrip()
  print(line) #lines
  print(type(line)) #str
  num = re.findall("([0-9]+)",line)
  print("num: ",num) #list
  for i in num:
    #print("i:",i)
    i = int(i)
    count.append(i)
print("There are", len(count), "values with a sum=", sum(count))
'''
#print(hand.read())
#print(type(hand.read()))
#print(type(line))
#print(re.findall("([0-9]+)", hand.read()))
