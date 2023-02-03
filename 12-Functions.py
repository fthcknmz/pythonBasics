# creating a function
def theFuction():
    print("Hey,i am a funciton")
#calling a function
theFuction()
# Arguments
def argFunc(argument):
    print(argument + " is the argument you gave")
argFunc("ddaa")
argFunc("xxyy")
print()
# if you do not know how many arguments that will be passed into your func. , add a * before the parameter name
def argFunc(*arguments):
    print(arguments[1] + " is the argument you gave")
argFunc("ddaa","xxyy")
print()
# Keyword Arguments
def argFunc(argument3,argument2,argument1):
    print(argument3 + " is argument3")
argFunc(argument1="a",argument2="aa",argument3="aaa")
print()
# if you do not know how many keyword arguments that will be passed into your func. add two asterix ** before the parameter name
def argFunc(**kid):
    print(kid["lastname"] + " is her last name")
argFunc(firstname="Hannah",lastname="Clara")
print()
# default parameter value
def theFunc(country="the World"):
    print("i am from "+country)

theFunc("Turkey")
theFunc("Germany")
theFunc()
theFunc("the USA")
print()
# Passing a list as an argument
def theFunc(food):
    for x in food:
        print(x)
fruits = ["apple","bannana","cherry"]
theFunc(fruits)
print()
#return values
def theFunc(x):
    return 5*x
print(theFunc(5)) #25
print(theFunc(0)) #0
print(theFunc(12)) #60
print()
# Recursion
def recursionFunc(x):
    if(x>0):
        return x*recursionFunc(x-1)
    else:
        return 1
    
    
print(recursionFunc(3))
print(recursionFunc(5))