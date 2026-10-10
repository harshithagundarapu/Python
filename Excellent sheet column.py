def convertToTitle(columnNumber):
    result = ""

    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        result = chr(65 + remainder) + result
        columnNumber //= 26

    return result


# Examples
print(convertToTitle(1))    # A
print(convertToTitle(28))   # AB
print(convertToTitle(701))  # ZY
