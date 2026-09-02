from datetime import date

dob = date(2007, 9, 7)
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Date of Birth:", dob.strftime("%d %B %Y"))
print("Age:", age)
