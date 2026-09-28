def file_read():
    try:                        # Error varum ennu predict cheyyunna caseil(like if else)
        filename=input("Enter filename:")       #kodukkunnathaanu(ee caseil illatha filename
        f = open(filename,"r")          #koduhtaal error varum but ippo file not exist varum)
        s = f.read()
        print(s)
        f.close()
    except:
        print("File does not exist")
        
def file_write():
    filename=input("Enter filename:")
    n = input("Enter the content:")
    f = open(filename,"w")
    f.write(n)
    f.close()
    
def file_append():
    filename=input("Enter the name of filename you need to edit:")
    n = input("Enter the content:")
    f = open(filename,"a+")
    f.write(n)
    f.seek(0)
    s=f.read()
    print(s)
    f.close()

def file_search():
    filename=input("Enter filename:")
    n=input("Enter the word to search:")
    f=open(filename,"r")
    s=f.read()
    if n in s:
        print("Word found")
    else:
        print("Word not found")
    f.close()
    
def file_delete():
    import os
    filename=input("Enter the name of filename you need to delete:")
    print("File",filename,"is deleted")
    os.remove(filename)
    


while(True):
    print("Menu Driven-File Operations")

    print("1.File read")
    print("2.File write")
    print("3.File append")
    print("4.File search")
    print("5.File delete")
    print("6.Exit")


    ch = int(input("Enter the choice:"))
    if ch == 1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    else:
        print("Exiting")
        break