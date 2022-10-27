
from time import localtime, strftime
t = localtime()
print(t)
print(t.tm_hour)
print(t.tm_min)
print(t.tm_sec)
print(strftime('%Y-%m-%d %H:%M:%S', t))

if t.tm_hour > 16:
    print("GÅ hem")
