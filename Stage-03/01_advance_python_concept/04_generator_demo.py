def generate_number():
    for i in range(1,11):
        yield i


get_num = generate_number()
print(next(get_num))

for i in get_num:       #i starts at 2
    print(i)