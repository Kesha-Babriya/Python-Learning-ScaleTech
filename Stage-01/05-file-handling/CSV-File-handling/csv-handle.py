import csv

students = [
    ['kesha',19],
    ['jash',17]
]

with open('students.csv','w',newline="") as file:
    write = csv.writer(file)

    write.writerow(['Name','Age'])
    write.writerows(students)


## READ 
with open('students.csv','r') as file:
    read = csv.reader(file)


    print("read data")
    head = next(read)       # next() moves cursor to next line nd return value
    print(f"Head = {head}")
    for row in read:
        print(row)


##APPEND

with open("students.csv",'a') as file:
    write = csv.writer(file)
    write.writerow(['SNESHA',21])