import urllib.request, urllib.parse, urllib.error
import beautifulsoup

html = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
soup = beautifulsoup(html, 'html.parser')
tags =soup('a')
for tag in tags:
    print(tag.get('href',None))
