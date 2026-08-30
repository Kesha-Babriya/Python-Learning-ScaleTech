try:
    age = int(input("Enter age "))
except ValueError:
    print("enter valid error")
else:
    print(f"Enter age is {age}")
finally:
    print("Code complete")


try:
    num = int(input("Enter num : "))
    list1 = [1,2,3,4,5]
    print(list1[num])
except IndexError:
    print("It is not valid index")
except ValueError:
    print("Enter valid input")
else:
    print(f"Your num is {num}")
finally:
    print("Always runs")


#Raise error

marks = int(input("Enter marks : "))
try:
    if marks<0 or marks>100:
        raise ValueError
except ValueError:
    print("Invalid marks")
else:
    print(f"Your marks is {marks}")