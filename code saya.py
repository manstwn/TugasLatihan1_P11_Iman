import math

a = lambda x: x**2

b = lambda x,y: math.sqrt(x**2+y**2)

c = lambda *args: sum(args)/len(args)

d = lambda s: "".join(set(s))

print(a(2))
print(b(2,3))
print(c(2,3,4))
print(d("DINA"))


