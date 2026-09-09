fib = [0, 1]

for i in range(2, 20):
    fib.append(fib[i - 1] + fib[i - 2])

print("The first 20 numbers of Fibonacci series are:")
print(*fib)
