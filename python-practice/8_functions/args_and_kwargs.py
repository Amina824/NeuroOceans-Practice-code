def total(*args):
    s = 0
    for i in args:
        s += i
    return s

print(total(1, 2))
print(total(1, 2, 3, 4, 5))


def info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

info(name="amina", roll=161, city="lahore")


def student(name, *subjects, **extra):
    print(name)
    print(subjects)
    print(extra)

student("amina", "math", "physics", age=20)

nums = [1, 2, 3]
print(total(*nums))
