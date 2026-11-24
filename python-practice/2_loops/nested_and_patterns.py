for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

print()

for i in range(1, 6):
    print("* " * i)

print()

for i in range(5, 0, -1):
    print("* " * i)

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
