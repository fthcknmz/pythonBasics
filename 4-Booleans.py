print(10>9) # returns true
print(10==9) # returns false
print(10<9) # returns false

a=300
b=22
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
print("\n***EVALUATE VALUES AND VARIABLES***") #EVALUATE VALUES AND VARIABLES
print("most values are true")# most values are true
print(bool("Hello"))
print(bool(9))
print(bool(["apple","bannana","cherry"]))
print("some values are false")# some values are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("\nisinstance() function \n")
x=200
print('is x an integer?: ',isinstance(x,int)) # check if x is integer or not
