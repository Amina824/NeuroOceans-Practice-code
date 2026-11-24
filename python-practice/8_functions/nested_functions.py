def calc(a, b):
    def add():
        return a + b

    def mul():
        return a * b

    print(add())
    print(mul())

calc(3, 4)


def make_multiplier(n):
    def m(x):
        return x * n
    return m

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))


def counter():
    c = 0

    def up():
        nonlocal c
        c += 1
        return c
    return up

count = counter()
print(count())
print(count())
