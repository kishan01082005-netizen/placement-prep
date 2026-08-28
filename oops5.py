class shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class circle(shape):
    def area(self):
        return 3.14 * (self.length ** 2)
    
class rectangle(shape):
    def area(self):
        return self.length * self.breadth
    
circle1 = circle(5, 0)
print("Area of circle:", circle1.area())
        
     