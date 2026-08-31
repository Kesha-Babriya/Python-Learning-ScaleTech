import todo as td


def main():

    while True:

        print("\n-------- Your To-Do List --------")
        print(
            "1. Add Task\n"
            "2. View Task\n"
            "3. Complete Task\n"
            "4. Delete Task\n"
            "5. Exit"
        )

        try:
            menu = int(input("Enter number for operation: "))

        except ValueError:
            print("Invalid input number.")
            continue

        if menu not in [1, 2, 3, 4, 5]:
            print("Enter a valid number.")
            continue

        if menu == 1:
            td.add()

        elif menu == 2:
            td.view()

        elif menu == 3:
            td.complete()

        elif menu == 4:
            td.delete()

        elif menu == 5:
            print("To-do list Closed.")
            break


if __name__ == '__main__':
    main()