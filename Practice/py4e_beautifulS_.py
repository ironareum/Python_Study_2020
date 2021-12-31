import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as TE 
import ssl

url ="http://py4e-data.dr-chuck.net/comments_42.xml"

#ignore SSL certificate errors
ctx = ssl.creat_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

request = urllib.request(url)


