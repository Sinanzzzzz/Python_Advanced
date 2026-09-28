#reverse the lines in a file

f = open('k.txt',"r")
s = f.readlines()

s.reverse()
print(s)

f.close()

f = open('k.txt',"w")       # Open in write mode to update inside the file
f.writelines(s)             #Output il "\n" must aanu for checking

f.close()