import urllib.request, urllib.parse, urllib.error
count =dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words =line.decode().split()
    for word in words:
        count[word] =count.get(word,0)+1
print(count)
