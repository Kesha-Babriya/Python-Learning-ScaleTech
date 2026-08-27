#tuple
tup = (1,2,3,4,3,5,6,'kesha')
tup1 = tup[-2:]     
print(tup1)
tup2 = (1,)     # type = tuple if (1)=> type int
print(type(tup2))

#reverse
print(tup[::-1])

#unpacking
tup2 = ('Conny',67)
first , second = tup2
print(first)
print(second)

#unpacking with * and it create as list
first , *middle , last = tup 
print(first)
print(middle)
print(last)

# Methods
print(tup.count(3))
print(tup.index(3))
print(tup.index(3,3,len(tup)))
