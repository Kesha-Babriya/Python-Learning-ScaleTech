from collections import Counter , namedtuple , defaultdict , deque

a = 'aaaaaaabbbbbbccc'

count1 = Counter(a)
print(count1)
print(count1.keys())
print(count1.values())
print(count1.items())
print(count1.most_common(1))
print(count1.most_common(2))
print(count1.most_common(1)[0][0])
print(count1.most_common(1)[0][1])
print(count1.most_common(2)[1][1])
print("Work as dict", count1['c'])
print("Convert into list", list(count1.elements()))

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count2 = Counter(numbers)
print(count2)

#------------------------------------------------------------------------------
#namedtuple
#User is class name and then its attributes(field names)

User = namedtuple("User","Name , Age")

u1 = User('kesha',20)

print(u1.Name)
print(u1.Age)

#-------------------------------------------------------------
#defaultdict

dict1 = {'java': 3,'python': 2}
d = defaultdict(int , dict1)    # can use anything like float , list , tuple , dict , bool

print(d['java'])
print(d['c'])


#--------------------------------------------------------------------------------

#deque

list1 = [3,4,5,6]
d = deque(list1)

print(d)

d.append(7)
d.appendleft(2)
print(d)

d.popleft()
d.pop()

print(d)

d.extendleft([2,1])

print(d)

d.rotate(2)     # rotate 2 step right

print(d)

d.rotate(-1)        # rotate 1 at left
print(d)