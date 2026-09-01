#self , __init__ ,__dict__
class Student:
    university = "MSU"

    def __init__(self, name, roll , marks):
        self.name = name
        self.roll = roll
        self.mark = marks
        print(f"{self.name} has {self.roll} roll no and {self.mark} marks ")

    def calculate_grade(self):
        if self.mark > 80:
            return "A-Grade"
        elif self.mark < 40:
            return "F-Grade"
        else :
            return "B-Grade"

    def is_passed(self):
        if self.mark > 40:
            print(f"{self.name} is Pass")
        else:
            print(f"{self.name} is Fail")


s1 = Student("kesha",3,89)
s2 = Student("abc",6,33)

print(s1.calculate_grade())
print(s2.calculate_grade())

s1.is_passed()
s2.is_passed()

##Class attribute

print(f"{Student.university} is access with class")

s1.university = "GTU"

print(f"After change class attribute, can access with object : {s1.university} ")

# dict give all information of that object in dictonary format
print("Dict of s1 object : ") 
print(s1.__dict__)

#-------------------------------------------------------------------------------------------  
## MRO using solution
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):          # check with D(C,B)
    pass

d = D()
print(D.mro())
d.show()