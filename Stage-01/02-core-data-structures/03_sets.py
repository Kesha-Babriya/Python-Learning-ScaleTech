numbers = {10,20,30,20,40}

print(numbers)      #duplicate removes , unordered
print(len(numbers))

if 30 in numbers:
    print("yes")

numbers.add("kesha")
numbers.remove(20)

#discard not throw error

a = {10,20,30}
b = {30,40,50}

print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))

# set comprehension
even = {number for number in a if number%2==0}
print(even)


#Exercise

club_a = ["Kesha", "Rahul", "Amit", "Priya", "Neha"]
club_b = ["Amit", "Priya", "Rohan", "Neha", "Jay"]

club_a = set(club_a)
club_b = set(club_b)

print(f"All unique students {club_a.union(club_b)}")
print(f"Students in both clubs {club_a.intersection(club_b)}")
print(f"Only Club A {club_a}")
print(f"Only Club B {club_b}")
print(f"Students in exactly one club {club_a.symmetric_difference(club_b)}")