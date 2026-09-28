class Category:
    def __init__(self):
        self.category_name = input("Enter the Category name:")
        
    def show_category(self):
        print("Name =",self.category_name)
        
class Product(Category):
    def __init__(self):
        super().__init__()
        self.product_name = input("Enter the product name:")
        self.price = int(input("Enter the price:"))
        self.quantity = int(input("Enter the quantity:"))
    def total_price(self):
        total = self.price*self.quantity
        print("Total price =",total)
        
p=Product()
p.show_category()
p.total_price()