s = input().split()

min_word = s[0]
max_word = s[0]

for word in s:
    if len(word) < len(min_word):
        min_word = word

    if len(word) > len(max_word):
        max_word = word

print(min_word)
print(max_word)
