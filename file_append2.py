
f = open("k.txt","a+")

print("First position",f.tell())
f.write("Python")

print("Second position",f.tell())
f.seek(0)

print("Third position",f.tell())
s = f.read()

print(s)
f.close()