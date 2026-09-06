from datetime import date

dob = date(2007, 9, 7)
today = date.today()

days = (today - dob).days

print("Days lived:", days)
