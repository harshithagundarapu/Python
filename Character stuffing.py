head = input("Enter character that represents the starting delimiter: ") 
tail = input(" Enter character that represents the ending delimiter: ") 
st = input("Enter the characters to be stuffed: ")
res=head 
for i in st:
     if i==head or i ==tail:
         res = res + i + i
     else:
         res = res + i 
res = res+tail
print("Frame after character stuffing: ", res)
