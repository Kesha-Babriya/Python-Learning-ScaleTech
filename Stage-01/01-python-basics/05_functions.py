#Multiple returns 
def calculate(a,b):
    return a+b,a-b
a,b = 7,5
add , sub = calculate(a,b)
print(f"Addition: {add} Substraction: {sub}")

#args , kwargs
def student_result(name, *args , **kwargs):
    print(f"Student name : {name}")
    total = 0
    for i in args:
        total += i
    
    print(f"Total marks is {total}")
    for key,value in kwargs.items():        # .items() extracts key value pair from kwargs dict
        print(f"{key}: {value}")

name = "kesha"
student_result(name,70,75,60,55,department="CSe",collage = "MSU")
