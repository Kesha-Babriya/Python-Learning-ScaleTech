class Person:
    
    def __init__(self,name , age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"{self.name} is {self.age} years old")

    def habit(self):
        print("persons'habit")

class Student(Person):
    def __init__(self ,name ,age, roll):
        super().__init__(name,age)
        self.rollN = roll

    def display_student(self):
        super().display_person()
        print(f"{self.name} has {self.rollN} roll number")
    def habit(self):
        print("Child -Student's overridden habit")

a = Student("kesha",20,5)
a.display_person()          # call parent method from child object
a.display_student()

print(isinstance(a,Student))
print(isinstance(a,Person))     # a is student and also a person


# method overriding

a.habit()
