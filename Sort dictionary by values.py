data = {"Maths": 85, "Science": 90, "English": 78}
sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_dict)
