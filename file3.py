# #write a program to update the second line in a file

f = open('k.txt',"r")

s = f.readlines()
s[1] = "Java" 
print(s)
f.close()


f = open('k.txt',"w")         # For updating the file(The question is to update the file)
f.writelines(s)               # File il change varum
f.close()