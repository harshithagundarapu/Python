pell = [0, 1]

for i in range(2, 20):
    pell.append(2 * pell[i - 1] + pell[i - 2])

print("The first 20 numbers of Pell series are:")
print(*pell)
