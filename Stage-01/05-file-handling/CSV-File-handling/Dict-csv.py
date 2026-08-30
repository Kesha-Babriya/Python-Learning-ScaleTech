import csv

student = [
    {'Name':'Kesha','Marks':97},
    {'Name':'Bella','Marks':82},
    {'Name':'Jere','Marks':57},
]


##WRITE 

fieldname = ["Name","Marks"]
with open("student2.csv",'w',newline="") as file:
    write = csv.DictWriter(file,fieldnames = fieldname)

    write.writeheader()
    write.writerows(student)

##append
with open("student2.csv",'a',newline="") as file:
    write = csv.DictWriter(file,fieldnames = fieldname)

    write.writerow({"Marks":65,"Name":"jenny"}) 
            #here i append in different order still appear in right order

#READ 
with open("student2.csv",'r') as file:
    read = csv.DictReader(file)

    highest = 0
    for row in read:
        if int(row['Marks']) >highest:
            highest = int(row["Marks"])
            name = row["Name"]

print(f"Highest marks of {name} is {highest}")