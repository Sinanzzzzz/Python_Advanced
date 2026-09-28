#Given a Dictionary
# 
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

try:
    d = {"name":"arun","age":23,"place":"ekm"}
    key = input("Enter a key:")
    print("Value =",d[key])
        
except KeyError:
    print("Key does not exist")