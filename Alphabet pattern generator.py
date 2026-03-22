n = 7  # size of grid
letter = input("Enter capital letter (A-Z): ")

for i in range(n):
    for j in range(n):

        if letter == 'A':
            if ((j == 0 or j == n-1) and i != 0) or \
               (i == 0 and j != 0 and j != n-1) or \
               i == n//2:
                print("*", end
