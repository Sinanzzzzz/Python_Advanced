#write a program to display the last 5 lines in a file

f = open('k.txt',"r")

s = f.readlines()
print(s[-5:]) 
f.close()