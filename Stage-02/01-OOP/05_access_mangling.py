class Student:
    def __init__(self,name,mark,password='123'):
        self.name = name
        self._mark = mark
        self.__pass = password
    
    def get_all(self):          #encapsulation
        print(f"{self.name} has {self._mark} marks nd password is {self.__pass}")
        

# access protected nd private
s1 = Student("kesha",87,'@123')
s1.get_all()
print(s1.name)
print(s1._mark)
print(s1._Student__pass)    

print(s1.__dict__)          # show all values in key value dictnories



#private can not override in child class

class Parent:

    def __init__(self):
        self.__value = "Parent"


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__value = "Child"


obj = Child()
print(obj.__dict__)     #shows two different attribut with same name but diffrent of class
        