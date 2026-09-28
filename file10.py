# Write a Python program to append the contents of one file into another text file

f = open('file2.txt', 'r')
s = f.read()
f.close()


f = open("file1.txt", "a")
f.write(s)
f.close()
 