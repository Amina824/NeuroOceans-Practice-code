s = {1, 2, 3, 3, 2}
print(s)

empty = set()
print(empty)

s.add(10)
print(s)

s.update([20, 30])
print(s)

s.remove(1)
print(s)

s.discard(100)
print(s)

s.pop()
print(s)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

print(3 in a)
print({1, 2}.issubset(a))

for i in a:
    print(i)

s.clear()
print(s)
