s = input().lower()
count = 0

for ch in s:
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print(count)
