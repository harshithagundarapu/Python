num = int(input("Enter decimal number: "))

print("1.Binary  2.Octal  3.Hexadecimal")
choice = int(input("Enter choice: "))

if choice == 1:
    print("Binary:", bin(num)[2:])
elif choice == 2:
    print("Octal:", oct(num)[2:])
elif choice == 3:
    print("Hexadecimal:", hex(num)[2:])
else:
    print("Invalid choice")
