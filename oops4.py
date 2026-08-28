
class vehicle:
    def start(self):
        print("Vehicle is starting")
        
class bike(vehicle):
    def ride(self):
        print("Bike is riding")
    
    
bike1 = bike()
print(bike1.start())
bike1.ride()