#write a python programm ro create a class name QuadatricEquation that represent a quadartricEquation of the form
#ax2+bx+c = 0
#attribute : private attribute __a,__b and__c to sore the coreEfficent of the quadatricEquation

#2.methods
    #a constructor to initialize the coreOfficent a,b and c
    #a privte method __discriminant that calculate and return a discriminant(D=b2-4ac)
    #s public method find_roots() that use the private discriminant method 
    #return the root of the quadatricEquation 
        #If D=0; one real root
        #if D>0; two distinct real root
        #IF d<0; two complex roots

import math

class QuadatricEquation:

    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __discriminant(self):
        return (self.__b*self.__b) - (4 * self.__a * self.__c)
    
    
    def find_roots(self):
        value = self.__discriminant()
        if value > 0 :
            root1 = ((-self.__b) + math.sqrt(value)) / 2*self.__a
            root2 = ((-self.__b) - math.sqrt(value)) / 2*self.__a
            return f"{root1} , {root2}"
        elif value < 0 :
            return "two complex roots"
        else :
            root = (-self.__b) / (2 * self.__a)
            return f"{root}"

x = QuadatricEquation(1,-3,-4)
print(x.find_roots())

    
