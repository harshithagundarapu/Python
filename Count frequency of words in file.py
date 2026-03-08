f = open("test.txt", "r")
words = f.read().split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
f.close()
