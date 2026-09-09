from datetime import date

dob = date(2007, 9, 7)
today = date.today()

birthday = date(today.year, 9, 7)

if birthday < today:
    birthday = date(today.year + 1, 9, 7)

days = (birthday - today).days

print("My next birthday is:", birthday.strftime("%d %B %Y"))
print("Days remaining:", days)
