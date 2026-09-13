from datetime import date

def calculate_age(day, month, year):
    dob = date(year, month, day)
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age

age = calculate_age(7, 9, 2007)

print("My age is:", age)
