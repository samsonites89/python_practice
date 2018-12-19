class Person:

    def __init__(self):
        self.name = "Bob"

    def set(self, name):
        self.name = name

    def __del__(self):
        print("PERSON DELETED") # you can see this get printed when the Person instance is deleted


class Student(Person):
    pass


p, s = Person(), Student()
print(isinstance(p, Person))  # True
print(isinstance(p, Student))  # false

print(isinstance(s, Person))  # True
print(isinstance(s, Student))  # True

bob = Student()
bob.set("bob")

print(bob.name)
