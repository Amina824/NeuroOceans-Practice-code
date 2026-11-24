def hello():
    print("hello")

hello()


def greet(name):
    print("hello", name)

greet("amina")


def add(a, b):
    return a + b

print(add(5, 6))


def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))


def power(a, b=2):
    return a ** b

print(power(5))
print(power(2, 3))


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(5))
