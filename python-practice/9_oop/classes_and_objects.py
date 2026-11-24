class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(self.name, self.roll)


s1 = Student("Amina", 161)
s2 = Student("Ali", 162)

s1.show()
s2.show()

print(s1.name)
s2.roll = 200
print(s2.roll)
