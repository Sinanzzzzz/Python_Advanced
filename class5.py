# create a class named Book with attributes title,author,price,pages,language
# and methods gettitle(),getauthor(),getprice(),settitle(),setauthor(),setprice()
# create a book object and call the methods

# b=Book()
# b.gettitle() #title
# b.settitle() #changes the object title

class Book:
    
    def __init__(self):
        self.title=input("Enter the title:")
        self.author=input("Enter the author name:")
        self.price=int(input("Enter the price:"))
        self.pages=int(input("Enter the no. of pages:"))
        self.language=input("Enter the language:")
        
    def gettitle(self):
        print("Title:",self.title)
        
    def getauthor(self):
        print("Author:",self.author)
        
    def getprice(self):
        print("Price:",self.price)
        
    def settitle(self):
        self.title = input("Enter the new title:")
        self.gettitle()
        
    def setauthor(self):
        self.author = input("Enter the new author:")
        self.getauthor()
      
    def setprice(self):
        self.price = int(input("Enter the new price:"))
        self.getprice()

b = Book()
b.gettitle()
b.getauthor()
b.getprice()
b.settitle()
b.setauthor()
b.setprice()