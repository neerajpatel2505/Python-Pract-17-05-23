class CartItem:
    def __init__(self,product,price,quantity):
        self.product=product
        self.price=price
        self.quantity=quantity

class ShoppingCart:
    def __init__(self):
        self.items=[]
    
    def add_item(self,product,price,quantity):
        item=CartItem(product,price,quantity)
        self.items.append(item)
        print("Item add successfully")
    
    def total_cost(self):
        total=0
        for item in self.items:
            total+=item.price*item.quantity
        print("Total cost:",total)
        
    def display_item(self):
        if len(self.items)==0:
            print("Cart is empty")
        else:
            for item in self.items:
                print(item.product,item.price,item.quantity)
    
    def remove_item(self,product):
        for item in self.items:
            if item.product==product:
                self.items.remove(item)
                print("--------item deleted successfully----------")
    
    def clear_cart(self):
        p=self.items
        p.clear()
        print("--------Clear cart successfully----------------")
        print("items:",self.items)
    
cart=ShoppingCart()
cart.add_item('Laptop',25000,1)
cart.add_item('Bag',250,10)
cart.add_item('Cable',25,25)
cart.total_cost()
cart.display_item()
cart.remove_item('Laptop')
cart.display_item()
cart.clear_cart()