#program to search a particular word in a file

f = open('k.txt',"r")

s = f.read()


if "Hello" in s:
    print("Character is present")
else:
    print("Character is not present")

# new = s.find("html")      # To find the position
# print(new) 

f.close()