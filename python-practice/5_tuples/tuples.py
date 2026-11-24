t = (10, 20, 30, 40, 50)
single = (5,)
empty = ()

print(t)
print(single)
print(empty)

print(t[0])
print(t[-1])
print(t[1:4])
print(t[::-1])

l = list(t)
l[0] = 100
t = tuple(l)
print(t)

a = (1, 2, 3)
b = (4, 5)
print(a + b)
print(a * 2)
print(2 in a)
print(len(a), max(a), min(a), sum(a))
print(a.count(2))
print(a.index(3))

x, y, z = a
print(x, y, z)

del t
