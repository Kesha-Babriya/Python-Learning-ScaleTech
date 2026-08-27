import random

print(random.randint(1,10))     #both include

print(random.randrange(1,10))       #10 is exclude
print(random.randrange(0,10,2))       #10 is exclude and possible values 0,2,4,6,8

print(random.random())          # between 0 and 1 . 1 is excluded

#select random from sequence
language = ['java','python','cpp']
print(random.choice(language))


#shuffle change order each time nd modify original list
number = [3,5,2,6]
random.shuffle(number)
print(number)
