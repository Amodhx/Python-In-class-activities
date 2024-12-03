# Class ekak defined krddi first letter ek capital use krnn
# e wageme camel case wlin define krnn
# class attribute defined krddi simple start
# Example

class CarItem:
    brand = ''
    year = ''

# how create function .
# when create function we have to add self always. because when we accesing class attributes we want to use self
    def setBrand(self,brand):
        self.brand = brand

# This is parameterize constructor
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    

    def display_values(self):
        print(self.brand,self.year)

    def update_values(self,brand,year):
        self.brand = brand
        self.year = year
        

    


# How crete object 
new_car = CarItem("TOYOTA",2006)

new_car.display_values()

# how access object item
new_car.brand = 'AUDI'
new_car.setBrand("BMW")
print(new_car.brand)
# print(new_car_2.brand)


# we can access class atttributes like this
print(CarItem.year)





