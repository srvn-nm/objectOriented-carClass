class Car :
    carsNumber = 0
    def __init__(self , brand , price , color) :
        self.carBrand = brand
        self.carPrice = price
        self.carColor = color
        self.status = False
        Car.carsNumber += 1
    def start(self) :
        if self.status == False :
            self.status = True
            print(f'the car of the brand {self.carBrand} starts working.')
        else :
            print(f'the car of the brand car {self.carBrand} is already working.')
    def stop(self) :
        if self.status == True :
            print(f'the car of the brand {self.carBrand} stops.')
        else :
            print(f'the car of the brand {self.carBrand} is not working now.')
    def off(self) :
        if self.status == False :
            print(f'the car of the brand {self.carBrand} is already off.')
        else :
            self.status = False
            print(f"the car {self.carBrand} turned off successfully.")
    def fulldetails(self) :
        if self.status == False :
            print(f'the car of the brand {self.carBrand} with the color {self.carColor} worths {self.carPrice}$ and it is off now.')
        else :
            print(f'the car of the brand {self.carBrand} with the color {self.carColor} worths {self.carPrice}$ and it is working now.')
car1 = Car(input("enter your car's brand here : ") , input("enter your car's price here : ") , input("enter your car's color here : "))
car1.fulldetails()
car1.stop()
car1.off()
car1.start()
car1.start()
car1.fulldetails()
car1.stop()
car1.fulldetails()
car1.off()
car1.fulldetails()
print(f'the number of added cars is {Car.carsNumber}.')