# A lambda function can take any number of arguments, but can only have one expression
# Syntax -->    lambda arguments : expression
x = lambda a: a+10 # add 10 to argument a
print(x(5)) 

# lambda functions can take any number of arguments
x = lambda a,b : a*b # add 10 to argument a
print(x(5,3)) 
print()

# usage in function
def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)
print(myDoubler(11))
myDoubler = myFunc(2)
print(myDoubler(20))
print()
myTripler = myFunc(3)
print(myTripler(11))
myTripler = myFunc(3)
print(myTripler(20))