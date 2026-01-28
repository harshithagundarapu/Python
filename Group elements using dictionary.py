lst = ["apple", "ant", "ball", "bat"]
result = {}

for word in lst:
    key = word[0]
    result.setdefault(key, []).append(word)

print(result)
