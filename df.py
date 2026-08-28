class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

samsung=mobile("galaxy",200000)
samsung.display()