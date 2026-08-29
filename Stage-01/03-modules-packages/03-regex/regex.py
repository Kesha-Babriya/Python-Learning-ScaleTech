import re

text = "I'm learning python"

#search()       only first occurance
result = re.search("python",text)
print(result)

if result:
    print('found')
else:
    print("not found")

result = re.search("java",text)     #gives Nona
print(result)

# match() => only check at begin otherwise none 

text ="python is good lang"
text1 =" python is good lang"

print(re.match("python",text))
print(re.match("python",text1))         #gives none becoz at begin there is space


#findall()      find all occurance

text = "Python is easy. Python is powerful."

print(re.findall("Python",text))
print(len(re.findall("Python",text)))       #how many occurance

#character regex

# 1 =\d
text = "My marks are 85 and my age is 19"
print(re.findall(r"\d",text))
print(re.search(r"\d",text))        #gives one digit at first occurance     ans=8
print(re.findall(r"\d+",text))
print(re.search(r"\d+",text))        #gives one or more digit at first occurance     ans=85

#2 = \s
print(re.findall(r"\s",text))

# 3 = \w find letter digit and _

text = "Python_123"
print(re.findall(r"\w",text))
print(re.findall(r"\w+",text))

#character set []

text = "cat bat rat"
print(re.findall(r"[bcr]at",text))      #[bcr] means find if b or c or r with at

text = "hello123"

print(re.findall(r"[a-z]+", text))      #match lower case letter


# ^ and $ and .

text = "Python is easy"

print(re.findall(r"^Py",text))      #if py at beginning or not
print(re.findall(r"^easy",text))      #if py at beginning or not


print(re.findall(r"Python$",text))      #if python at end or not
print(re.findall(r"easy$",text))        

print(re.findall(r"P.t",text))

# .sub()

text = "My phone number is 12345"

print(re.sub(r"\d+","XXX",text))


# .split()

text = "Python,Java;C++"

result = re.split(r"[,;]", text)

print(result)