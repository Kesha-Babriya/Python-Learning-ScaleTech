from itertools import product , permutations , combinations , accumulate
import operator as op  # for accumulate

# product
print("--------Product-------")
a = [1,2]
b = [3,4]
ans = list(product(a,b))
print((ans))
print(ans[1])

b = [3]
ans2 = product(a,b,repeat = 2)
print(list(ans2))

#-------------------------------------------

#permutations => order matter

print("--------Permutations-------")

a = [1,2,3]
perm = permutations(a)
print(list(perm))

prem = permutations(a, 2)
print(list(prem))


#---------------------------------
#combinations => order does not matters

print("--------Combinations-------")

a = [1,2,3,4]

comb = combinations(a,2)    # provide length is mandatory
print(list(comb))

comb = combinations(a,3)    # provide length is mandatory
print(list(comb))

#-------------------------------------------------

#accumulate => make arithmatic in the list by default = add operation

print("-----------Accumulate-----------")

number = [1,2,3,4,5]
addN = accumulate(number)

print("Original number" , number)
print("By default addition in list" , list(addN))

mulN = accumulate(number , op.mul)

print("Original number" , number)

print("Multiplication ",list(mulN))

number = [1,2,5,3,4]
print("Original number" , number)

list1 = accumulate(number , func= max)
print("Max print", list(list1))
