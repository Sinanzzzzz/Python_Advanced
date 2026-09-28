# A file totalstudents.txt contains the names of all students in a class, 
# # and a file passedstudents.txt contains the names of students who passed.txt the exam. 
# # Write a Python program to: # Read the names from both files. 
# # # Find the students who did not pass. 
# # # Write their names to a new file named failed_students.txt, one name per line. 


f = open("totalstudents.txt","r")
total=f.readlines()
print(total)


g = open("passedstudents.txt","r")
passed=g.readlines()
print(passed)


h = open("failed_students.txt","w")

for i in total:
    if i not in passed:
        h.write(i)
        
f.close()
g.close()        
h.close()