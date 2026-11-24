class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("i am", self.name, "and i am", self.age)


class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def show_roll(self):
        print("roll no is", self.roll)


class Teacher(Person):
    def intro(self):
        print("i am a teacher, my name is", self.name)


s = Student("Amina", 20, 161)
s.intro()
s.show_roll()

t = Teacher("Sir Ahmed", 40)
t.intro()
