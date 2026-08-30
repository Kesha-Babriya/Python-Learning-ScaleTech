print("----------Calculator----------")
run = 'y'
while run =='y' or run == 'Y':
    try:
        n1 = int(input("Enter first number as input: "))
        op = input("Enter Operator for Operation like (+ , - ,* , / , % ): ")
        n2 = int(input("Enter second number as input: "))
    except ValueError:
        print("Enter valid input")
    else:

        possibleOperator = ['+','-','*','/','%']
        try:
            if op not in possibleOperator:
                raise ValueError

        except ValueError:
            print("Invalid Operator . Can not perform operation")
        else:
            print(f"Your numbers are {n1} and {n2} and you want to perform {op}")

            try:
                if op == '+':
                    result = n1 + n2
                elif op == '-':
                    result = n1 - n2
                elif op == '*':
                    result = n1 * n2
                elif op == '/':
                    result = n1 / n2
                else:
                    result = n1 % n2

            except ZeroDivisionError:
                print("Can not divide by zero")
            else:
                print(f"Result : {n1} {op} {n2} = {result}")
                try:
                    run = input("Do you want to continue? (y/n): ")
                    check = ['y','n','Y','N']
                    if run not in check:
                        raise ValueError
                except ValueError:
                    print("Enter valid Reply for continue")
                else:
                    if run == 'n' or run =="N":
                        print("Calculator Closed. ")