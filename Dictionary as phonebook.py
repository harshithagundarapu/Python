phonebook = {"Alice": 1234, "Bob": 5678}
name = input("Enter name: ")

if name in phonebook:
    print(phonebook[name])
else:
    print("Not found")
