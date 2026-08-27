import datetime

# current date and time
print(datetime.datetime.now())

#date
print(datetime.date.today())


#Access individual part
now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)


# create a specific date,time
date = datetime.date(2026,9,6)
time = datetime.time(14, 30, 45)

print(time)
print(date)

#formate time
print(now.strftime("%d-%m-%Y"))