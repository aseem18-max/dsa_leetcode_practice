import time
a = time.time()
x = int(input())
if str(x)[::-1] == str(x):
    print(True)
else:
    print(False)
print(time.time()-a)
b=time.time()
strx = str(x)
reversex = str(x)[::-1]
print(strx==reversex)
print(time.time()-b)