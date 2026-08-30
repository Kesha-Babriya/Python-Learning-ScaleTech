##Create student.txt using Python and store:

# create mode - 'x'     if file exist gives error
# with open('student.txt','x') as file:
#     file.write("Hello make file from python file \nHello from Keshaaa!!!")


# list1 = ['\nNoah\n','Nick\n','Conny\n']
# with open('student.txt','a') as file:
#     file.writelines(list1)            #writelines write list

#read mode

file = open('student.txt','r')
data = file.read()      #read all file data 

print(data)
file.seek(0)  
         #cursor move back to begin
data = file.readline()
print(f"Using readline {data}")

file.seek(0)
print("Using loop , traverse line by line")
for line in file:
    print(line)
file.close()