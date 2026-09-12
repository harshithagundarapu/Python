from datetime import date

dob = date(2007, 9, 7)

print("Day of the year:", dob.timetuple().tm_yday)
