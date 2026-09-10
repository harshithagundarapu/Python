from datetime import date

dob = date(2007, 9, 7)
today = date.today()

if today.day == dob.day and today.month == dob.month:
    print("🎂 Happy Birthday to me! 🎉")
else:
    print("Today is not my birthday.")
