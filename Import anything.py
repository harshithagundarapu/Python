# Open a CSV file in write mode
file = open("students.csv", "w")

# Write the header row
file.write("Name,Register Number,Mobile Model\n")

# Get details for 5 students
for i in range(1, 6):
    print(f"\nEnter details for Student {i}:")
    name = input("Enter Name: ")
    reg_no = input("Enter Register Number: ")
    mobile = input("Enter Mobile Model: ")

    # Write each student's details to the file
    file.write(f"{name},{reg_no},{mobile}\n")

# Close the file
file.close()

print("\nStudent details have been successfully saved to 'students.csv'.")
