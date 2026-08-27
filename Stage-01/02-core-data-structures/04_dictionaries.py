student = {
    'name':'kesha',
    'age':'19',
    'department' : 'CSE',
    'collage' : 'MSU'}

#Access key nd values
print(student['name'])
print(student.get('marks'))     #does not throw error
print(student['age'])
print(student.values())
print(student.keys())
print(student.items())

#modify existing value

student['age'] = 20

#Nested dictonary

info = {
    'student1' : {
        'name' : 'Nick',
        'marks' : 98
    },
    'student2' : {
        'name' : 'Noah',
        'marks' : 76
    }
}
 # for traverse in nested dict

for studentid,details in info.items():
    print(studentid)
    for key, value in details.items():
        print(f"{key} : {value}") 

#Method 2 for traverse

for studentid,details in info.items():
    if details['marks']>90:
        print(f"{studentid} name is {details['name']} is  pass with marks {details['marks']}")
    else:
        print(f"{studentid} name is {details['name']} is  fail with marks {details['marks']}")

# dictionary comprehenstion as key value pair
list1 = [1,2,4,5]
dictcomp = {x*2:x*x for x in list1}
print(dictcomp)