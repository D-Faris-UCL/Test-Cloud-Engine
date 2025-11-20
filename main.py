import time

a = time.localtime().tm_sec
b = time.localtime().tm_min
c = a+b

print(a)
print(b)

for i in range(10):
    c = a+b
    a = b
    b = c
    print(c)