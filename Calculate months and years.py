from datetime import date

dob = date(2007, 9, 7)
today = date.today()

years = today.year - dob.year
months = today.month - dob.month

if today.day < dob.day:
    months -= 1

if months < 0:
    years -= 1
    months += 12

print("Years:", years)
print("Extra Months:", months)
