l = [10, 20, 30, 40, 50, 60]

del l[0]
print(l)

del l[1:3]
print(l)

l.remove(60)
print(l)

x = l.pop()
print(x, l)

l.clear()
print(l)
