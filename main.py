import time

a = time.localtime().tm_sec
b = time.localtime().tm_min
c = a+b

print(a,flush=True)
print(b,flush=True)

for i in range(100):
    c = a+b
    a = b
    b = c
    print(c,flush=True)