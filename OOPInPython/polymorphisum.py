# Polymorphisum with python
# It allows objects of different classes to be treated as objects of a common super class, and it enables you to write more
# flexible and reusable codes


# Encapsulation with python 

# Access modifiers in python
# class Main:
#     name = '' #public
#     _age = '' #protected (one ( _ ))
#     __city = '' #private (two ( _ ))



class Encapsulation:
    __private_var = 'Private'

    def set_value(self,value):
        self.__private_var = value
    def get_value(self):
        return self.__private_var



class_instance = Encapsulation()
print(class_instance.get_value())
class_instance.set_value("SETTED VALUE")

print(class_instance.get_value())

