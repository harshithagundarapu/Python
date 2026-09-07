from datetime import date

dob = date(2007, 9, 7)
today = date.today()

days = (today - dob).days
weeks = days // 7

print("Weeks lived:", weeks)
