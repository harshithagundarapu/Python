year = 2007

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("2007 is a leap year")
else:
    print("2007 is not a leap year")
