import httplib
# conn = httplib.HTTPSConnection("https://picoctf.com/")
conn = httplib.HTTPSConnection("picoctf.com", 443)
conn.request("GET", "/")

r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()
conn.request("GET", "/")
r2 = conn.getresponse()

print(r2.status, r2.reason)
data2 = r2.read()
conn.close()