# # #write a program to display the number of words in a file 

f = open('k.txt',"r")

s = f.read()
print(s.split())
print(len(s.split()))


f.close()