#Class-based Context Manager
class StudentFileManager:
    def __init__(self,mode):
        self.mode=mode
        self.filename = "context.txt"
    def __enter__(self):            #automatic runs when with block run
        print("Opening student file..")
        self.file = open(self.filename,self.mode) 
        return self.file
    def __exit__(self, exc_type, exc, traceback):   #it runs when with ends    #when everything work normal last 3 has none value
        print("Close student file")
        print("Exception type:", exc_type)
        print("Exception:", exc)
        print("Traceback:", traceback)
        self.file.close
        return True         #it handle exception nd runs further code without error

        #if we do not write True then after end of exit block it blocks further execution

with StudentFileManager('w') as f:
    print("Processs student file")
    f.write("before exeception")
    divide = 10/0       #if error occure program dont stop it start execute __exit__ method
    f.write("Hello from context manager")   #it not runs


print("program continued after execution")
#A @contextmanager-based context manager

from contextlib import contextmanager

@contextmanager
def student_session():
    print("Starting student session...")
    mess = 'hello'
    yield mess    #Give control to the with block. also pass object to with block
    print("Student session finished.")      #after end of with block control move after yield

with student_session() as msg:
    print(msg)
    print("Student session running")