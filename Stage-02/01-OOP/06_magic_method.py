
# __str__ and __repr__
class Book:
    def __init__(self,name , price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Book {self.name} has ${self.price} price"

    def __repr__(self):
        return f"Book('{self.name}' , {self.price})"


b1 = Book('Java','500')

print(b1)       # calls __str__ if not available then execute __repr__
print([b1])     # calls __repr__

# ALL COMPARISON DUNDER METHOD

class Student:
    def __init__(self,name,marks,subjects):
        self.name = name
        self.marks = marks
        self.subjects = subjects
    def __eq__(self, other):
        return self.name == other.name and self.marks == other.marks
    def __ne__(self, other):
        return  self.marks != other.marks
    def __lt__(self, other):
        return self.marks < other.marks
    def __le__(self, other):
        return self.marks <= other.marks
    def __gt__(self, other):
        return self.marks > other.marks
    def __ge__(self, other):
        return self.marks >= other.marks
    def __len__(self):
        return len(self.subjects)
    def __contains__(self , sub):
        return sub in self.subjects
    def __getitem__(self,index):
        return self.subjects[index]


s1 = Student("A",87,'java')
s2 = Student("A",67,'py')
print(s1 == s2)
print(s1 != s2)
print(s1 > s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 < s2)

# __len__ and __contains__ and __getitem__  and __setitem__


s3 = Student('C',89,['java','py','c','cpp'])
print("Length of subject is ",len(s3))
print("Check contains dunder method ==>",'c' in s3)
print("Item at 1 index ==>" , s3[1])

# add , sub , mul

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, number):
        return Money(self.amount * number)

    def __str__(self):
        return f"₹{self.amount}"


m1 = Money(500)
m2 = Money(300)

print(m1 + m2)
print(m1 - m2)
print(m1 * 2)