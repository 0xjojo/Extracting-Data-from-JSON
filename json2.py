import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
num = 0
sum = 0
url = input ("Enter location:")
html = urllib.request.urlopen(url, context=ctx).read()
print ("Retrieving" , url)
print ("Retrieved" , len(html) , "characters")
info = json.loads(html)

#print (info)
lst = info["comments"]
print('Count:', len(lst))

for item in lst :
    num = int(item["count"])
    sum = sum + num
print ("Sum:" , sum)
