# Nestad  function 

# def outer(x) :
#     def inner(y):
#         return x + y
#     return inner

# print(outer(5)(10))


# def add(x,y):
#     return x+y

# def calculate(func,x,y):
#     return func(x,y)

# result = calculate(add,10,22)

# print(result)


# without decorators
def make_pretty(func):
    def inner():
        print("I Got Decorated")
        func()
    return inner

def ordinary():
    print("I Am Ordinary ")

get_decorated = make_pretty(ordinary)
get_decorated()


# with decorators
def make_pretty(func):
    def inner():
        print("i go decoraterd")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()
