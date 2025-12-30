print("1.C to F  2.F to C")
ch = input("Choose: ")

if ch == '1':
    c = float(input("Celsius: "))
    print((c * 9/5) + 32)
elif ch == '2':
    f = float(input("Fahrenheit: "))
    print((f - 32) * 5/9)
