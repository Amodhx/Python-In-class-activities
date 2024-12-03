
# Inheritance in Python
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} syas Meow! "
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof! "

cat = Cat("Cat")
print(cat.speak())

dog  = Dog("Dog")
print(dog.speak())