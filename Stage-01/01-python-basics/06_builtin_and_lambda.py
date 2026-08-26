# Sorted function with lambda
marks = [60,50,89,43,23]
sort_n = lambda x: sorted(x)
reverse = lambda x: sorted(x,reverse=True)
print(f"Original : {marks}\nSorted: {sort_n(marks)}\nReverse: {reverse(marks)}")
print(f"Max: {max(marks)}\nMin: {min(marks)}\nSum: {sum(marks)}\nAvg: {sum(marks)/(len(marks))}")

names = ['kesha','jash','abc','xyz']



#zip
for name,mark in zip(names,marks):
    print(name,mark)


#enumerate() gives (index,value) 
for i,mark in enumerate(marks,start=1):
    if mark>50:
        print(f"{i}: {mark}-Pass")
    else:
        print(f"{i}: {mark}-Fail")


# isinstance()

a = "10"
print(isinstance(a,int))    #False
print(isinstance(a,(int,str)))      #check from this two 