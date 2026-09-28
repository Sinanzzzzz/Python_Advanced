# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

try:
    filename = input("Enter the filename to open:")
    f = open(filename,"r")
    s = f.read()
    
except FileNotFoundError:
    print("File does not exist" )

else:
    print(s)
    f.close()