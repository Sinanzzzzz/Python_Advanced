#find the number of letters,digits,and spaces in a file 

f = open('k.txt',"r")
s = f.read()

letters_count = 0
digits_count = 0
spaces_count = 0

for i in s:
    if i.isalpha():
        letters_count += 1
    elif i.isdigit():
        digits_count += 1
    else:
        spaces_count += 1
        

print("The number of letters =",letters_count)
print("The number of digits =",digits_count) 
print("The number of spaces =",spaces_count) 
 
f.close()