from datetime import date

dob = date(2007, 9, 7)
today = date.today()

days = (today - dob).days
hours = days * 24
minutes = hours * 60

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
