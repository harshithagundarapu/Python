with open("sample.txt", "r") as file:
    text = file.read()

print("Words:", len(text.split()))
