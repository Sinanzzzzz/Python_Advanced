# # #write a program to read a text file and displays the number of lines in a file
f = open('k.txt',"r")

s = f.readlines()

print(len(s))

f.close()