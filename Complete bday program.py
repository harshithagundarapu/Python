from datetime import date

day = 7
month = 9
year = 2007

dob = date(year, month, day)
today = date.today()

age = today.year - year

if (today.month, today.day) < (month, day):
    age -= 1

birthday = date(today.year, month, day)

if birthday < today:
    birthday = date(today.year + 1, month, day)

days_left = (birthday - today).days

print("╔════════════════════════════╗")
print("║       MY INFORMATION       ║")
print("╠════════════════════════════╣")
print("║ DOB       :", dob.strftime("%d %B %Y"))
print("║ Born On   :", dob.strftime("%A"))
print("║ Age       :", age)
print("║ Next B-Day:", birthday.strftime("%d %B %Y"))
print("║ Days Left :", days_left)
print("╚════════════════════════════╝")
