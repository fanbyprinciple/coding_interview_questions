import hashlib
import sys

f = open('rockyou.txt', mode="r", encoding='latin-1')

try:
    # lines = [i.decode('utf-8') for i in f.readlines()]
    lines = [i for i in f.readlines()]
except Exception as e:
    print(e)
    sys.exit(0)

for line in lines:
        print('Checking for ', line)
        if(hashlib.sha256(line.encode()).hexdigest() == 'e7ae6cfee91a324590df7b048dcc9802b7389c1b0d996d474d61c4cbb1253455'):
            print('password is : ', line)
            break
    
# print(hashlib.sha256("hello_12345".encode()).hexdigest())