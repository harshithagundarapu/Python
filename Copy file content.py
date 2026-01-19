f1 = open("a.txt","r")
f2 = open("b.txt","w")

f2.write(f1.read())

f1.close()
f2.close()
