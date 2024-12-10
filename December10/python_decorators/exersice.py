# write a python program
    # Create a decorator check_positive
        #   That check if the input number is a positive number
        #   If the input is not positive print a messege line "Input must be a positive number"
    
    #Use this decorator on the function calculater sqare_root that 
        #  Case one number and input
        #  Retrurns the squar_root of the input 

import math
def check_positive(func):
    def inner(number):
        if number > 0 :
            func(number)
        else:
            print("Input must be a positive number")
    return inner
    

@check_positive
def calculater_square_root(number) :
    return math.sqrt(number)

number = int(input("Enter a Number: ")) 
calculater_square_root(number)

