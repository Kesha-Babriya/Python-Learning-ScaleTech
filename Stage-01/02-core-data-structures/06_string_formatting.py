text = 'python Programming'

# slicing 
print(text[0])
print(text[:6])
print(text[:11])
print(text[::-1])
print(text[::2])

text = '        python Programming  '

text = text.rstrip()        # right strip only
print(text)
text = text.strip()
print(text)
print(text.title())
print(text.upper())
print(text.lower())

print(text.replace("python",'java'))

print(text.split())         # string to list

list1=['java','python']
print("/".join(list1))      # list to string

print(text.index('Pr'))
print(text.count('m'))


print(text.startswith("py"))
print(text.endswith("ing"))

text = "python "

print(text.islower())
print(text.isupper())
print(text.isspace())       #only space
print(text.isalpha())       # only alpha ,no space

text = 'py143HG'

print(text.isalnum())


#Formatting

score = 0.8756
print(f"{score:.2%}")       # % formate

salary = 1500000
print(f"{salary:,}")        #thousands separate

##simple CLI table

students = [
    ("Kesha", 19, 87.5),
    ("Rahul", 20, 91.25),
    ("Amit", 19, 76.8)
]

print("--------CLI Table--------")
print(f"{'Name':<10}{'Age':<10}{'Marks':<10}")
for id in students:
    print(f"{id[0]:<10}{id[1]:<10}{id[2]:<10,.2f}")