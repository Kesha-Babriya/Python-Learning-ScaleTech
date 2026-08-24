#Control flow
marks = int(input("Enter marks: "))
if marks>90:
    print("Excellent")
elif marks>80 and marks<=90:
    print("Good")
else:
    print("Try to improve")

#Loops
for i in range(3):
    print(i)

for i in range(2,6,2):
    print(i)

for i in range(8,0,-2):
    print(i)

i=1
while i<3:
    print(i)
    i += 1

word = "python"
for ch in word:
    print(ch)