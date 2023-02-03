# Scope is a variable that is only available from inside the region it is created.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function
def myFunc():
    x = 400
    print(x)
myFunc() # a ariable created inside a funciton is available inside that function
# print(x) using x in here will raise an error: name 'x' is not defined
print()
#A function inside a function
def myFunc():
    x = 600
    def innerFunc():
        print(x)
    innerFunc()
myFunc()
print()
#Global Scope
x = 800 # can be used by anyone
def myFunc():
    print(x)
myFunc()
print(x)
print()
# if you oparete with the same variable name inside and outside of a function, Python will treat them as two separate variables
x = 1000
def myFunc():
    x = 1220
    print(x)
myFunc()
print(x)
#Global keyword
def myFunc():
    global x  # makes x a global variable
    x = 1
    print(x)
myFunc()
print(x)
print()
#to change the value of a global variable inside a function
x = 5
def myFunc():
    global x
    x = 200
    print(x)
myFunc()
print(x)