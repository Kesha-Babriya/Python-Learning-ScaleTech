# list nd it's method

students = ['isabella','noah','nick','conny']
print(f"first is {students[0]}, last is {students[-1]}")
print(students)
students[1] = 'jeremiah'    #change value
students.append('kesha')    #append at last
print(students)
students.insert(1,True)     #insert at any index
print(students)
students.remove('jeremiah')     #remove() method
print(students)
print(len(students))    #length

if 'nick' in students:          # in and not in
    print("yes nick in student")

#slicing
print(students[1:3])  
print(students[:4:2])   #with jump 

#nested list

marks = [[11,22,33],[44,55]]
print(marks[0][1])

#list comprehension
numbers = [1,2,3,4,5]

squares = [i*i for i in numbers]
even = [i for i in numbers if i%2==0]

print(squares)
print(even)