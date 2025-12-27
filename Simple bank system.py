balance = 1000

while True:
    print("1.Deposit  2.Withdraw  3.Balance  4.Exit")
    ch = input("Choose: ")

    if ch == '1':
        balance += int(input("Amount: "))
    elif ch == '2':
        balance -= int(input("Amount: "))
    elif ch == '3':
        print("Balance:", balance)
    elif ch == '4':
        break
