
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


    def __init__(self, name,color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} says woof! and its clr {self.color}"

cat = Cat("Cat")
print(cat.speak())

dog  = Dog("Dog","Black")
print(dog.speak())