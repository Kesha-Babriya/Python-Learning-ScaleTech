import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "to_do.csv")

def add():

    task = input("Enter task in list: ")

    with open(CSV_FILE, "a", newline="") as file:

        write = csv.writer(file)

        write.writerow([task, "Pending"])

    print(f"Task '{task}' is added successfully.")
    

def view():

    print("\n-------- Your Tasks --------")

    with open(CSV_FILE, "r", newline="") as file:

        read = csv.reader(file)

        tasks = list(read)

    if len(tasks) <= 1:
        print("There is no task.")
        return

    for index, row in enumerate(tasks[1:], start=1):

        print(f"{index}. {row[0]} [{row[1]}]")


def complete():

    view()

    try:
        num = int(input("Enter task number to mark completed: "))

    except ValueError:
        print("Invalid number.")
        return

    with open(CSV_FILE, "r", newline="") as file:

        read = csv.reader(file)
        tasks = list(read)

    if num < 1 or num >= len(tasks):
        print("Invalid task number.")
        return

    tasks[num][1] = "Completed"

    with open(CSV_FILE, "w", newline="") as file:

        write = csv.writer(file)
        write.writerows(tasks)

    print("Task marked as completed.")

def delete():
    view()
    list1 = []
    try:
        num = int(input("Enetr task number which you want to delete: "))
    except ValueError:
        print("Invalid number")
        return
    
    with open(CSV_FILE,'r') as file:
        read = csv.reader(file)
        list1 = list(read)

        if num < 1 or num >= len(list1):
           print("Invalid number")
           return 

        deleted = list1.pop(num)
        
        with open(CSV_FILE,'w', newline="") as file:
            write = csv.writer(file)
    
            write.writerows(list1)
            print(f"Task {deleted} deleted successfully")
            
