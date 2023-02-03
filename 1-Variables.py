print('\n***CREATING VARIABLES***') # CREATING VARIABLES
x = 9   # is of type int
y = "Fethi"  # is of type str
print(x) # will print '9'
print(y) # will print 'Fethi'

x = "is a human" # is now of type str
print(y,x)  # will print 'Fethi is a human'

print('\n***CASTING***') # CASTING
a = str(3)
b = int(3)
c = float(3)
print(a,b,c,'\n') # will print all as 3

res1=b+c 
print('res1=',res1)

res2=b+int(a) #  res2=b+a gives TypeError (a is a string so we need to convert it to integer) --unsupported operand type(s) for +: 'int' and 'str'--
print('res2=',res2)

print('\n***GETTING TYPE***') # GETTING TYPE
x=5
y="Fethi"
z=7.0
print('type of x is ',type(x))
print('type of y is ',type(y))
print('type of z is ',type(z))

print('\n***SINGLE OR DOUBLE QUOTES***') # SINGLE OR DOUBLE QUOTES
a= "Fethi" 
#is same as
b= 'Fethi'
print('a:',a,'b:',b)

print('\n***CASE-SENSITIVE***') # CASE-SENSITIVE
a=9
A="Fethi" # A is not overwrite a
print('a:',a,'A:',A)

print('\n*** MANY VALUES to MULTIPLE VARIABLES***') # MANY VALUES to MULTIPLE VARIABLES
x, y, z = "Orange", "Banana", "Cherry"
print('x:',x, 'y:',y, 'z:',z)

print('\n*** ONE VALUE to MULTIPLE VARIABLES***') # ONE VALUE to MULTIPLE VARIABLES
x = y = z = "Watermelon"
print('x:',x, 'y:',y, 'z:',z)

print('\n***UNPACKING A COLLECTION***') # UNPACKING A COLLECTION
# if you have a collection of values in a list, tuple etc. Python allows you extract these values into variables which is called unpacking 
animals = ["cat","dog","mice"]
x,y,z = animals # unpacking section
print('x',x)
print('y',y)
print('z',z)

print('\n***OUTPUT VARIABLES***') # OUTPUT VARIABLES
x = "Fethi"
y = " is coding"
z = x + y
print(z) # will add y to end of x
x = 5
y = 6
z = x + y
print(z) # will sum x and y
x = "Fethi"
y = 6
z = x + str(y) # z = x + y gives TypeError --can only concatenate str (not "int") to str--
print(z)

print('\n***GLOBAL VARIABLES***') # GLOBAL VARIABLES
# Variables that arre created outside of a function are known as global variables
# Global variables can be used both inside and outside of functions
k=" is coding" # global variable
def aFunc():
        l="Fethi" # local variable
        print(l + k)
aFunc()
# print(l + k) gives NameError --name 'l' is not defined--

print('\n***THE global KEYWORD***') # THE global KEYWORD

def anotherFunc():
    global l # makes l a global variable
    l="Fethi"
    print(l + k + '   (inside of the function)')
anotherFunc()
print(l + k + '   (outside of the function)')