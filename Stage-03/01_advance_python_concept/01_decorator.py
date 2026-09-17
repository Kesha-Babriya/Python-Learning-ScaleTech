import time
from functools import wraps

#example 1
print("Student Result with decorator")

def decorator_with_args(min_mark):      #outer handle passing argument
    def decorator_handle_func(func):        #handle function result
        @wraps(func)                #decorator used inside custom decorators to preserve the original function's metadata like docstring
        def wrapper(*args , **kwargs):
            start = time.time()
            print("----Starting---")
            name,result = func(*args , **kwargs)
            print("----Ending----")
            if result >= min_mark:
                print(f"{name} is pass with {result:.2f}%")
            else:
                print(f"{name} is failed with {result:.2f}%")
            end = time.time()
            print(f"Execution time is {end - start:.4f} seconds")
            print(f"Use of wraps that store metadata {func.__name__} and docstring is {func.__doc__}")
        return wrapper
    return decorator_handle_func




@decorator_with_args(40)        #3 layer becomes becoz it passes args
def result(name , *marks):
    '''Docstring of result'''
    total = sum(marks)
    result = total / len(marks)
    return name,result

print(f"use of wraps again {result.__doc__}")       # preserves the all data in wraps

result("kesha",32,35,30)

#Example 2
print("Decorator example 2 multiple decorators..")
def first(func):

    def wrapper():
        print("First Before")
        func()          #this runs second(greet) becoz func = second(greet)
        print("First After")

    return wrapper


def second(func):

    def wrapper():
        print("Second Before")
        func()
        print("Second After")

    return wrapper

@first
@second
def greet():
    print("Hello")
greet()         #here call first(second(greet))

