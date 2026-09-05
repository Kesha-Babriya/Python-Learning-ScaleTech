from functools import partial , reduce , lru_cache

#partial() create new function with some fixed argument

print("----------partial-------")
def mult(x , y) :
    return x * y

# if i want to mul by 2 all number 
# had to do mult(2,3)...

double = partial(mult , 2) 

for i in range(1,5):
    print(f"{i} * 2 ==> {double(i)}")

#--------------------------------------------------------

#reduce = repeatedly applies a function to the elements of an iterable(list ,..etc) and produces one final result.

print("----------reduce-------")
number = [2,3,4,5]
result = reduce(mult , number)
# result = reduce (lambda a,b: a*b , number)
print(result)

#----------------------------------------------------------
#lru_cache() is a decorator that caches function results.

print("--------------lru_cache---------")
print("Here you see exaple how it reuse the stored ans nd not execute the function")

@lru_cache(maxsize=5)
def square(n):
    print("Calculating....")
    return n * n

print(square(5))
print(square(5))

print(square(5))
print(square(5))
print("After one execution it only print the answer")