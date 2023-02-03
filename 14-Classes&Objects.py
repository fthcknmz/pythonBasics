# To create a class use class keyword
class MyClass:
    x=6
#To create an object using MyClass
MyObj = MyClass()
print(MyObj.x)
print()
# Create a class named Person, use the __init__() function to assig values for name and age
class Person:
    def __init__(self,name,age): # __init__() function is called automatically every time the class is being used to create a new object
        self.name = name
        self.age = age
person1 = Person("Fethi",20)
print(person1.name)
print(person1.age)
# Object Methods
class Person:
    def __init__(self,name,age): # self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
        self.name = name
        self.age = age
        
    def Func(self):
        print("Hello dear, i am " + self.name)
        
person1 = Person("Fethi", 20)
person1.Func()
# it doesnt have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class
class Person:
    def __init__(sillObject, name, age):
        sillObject.name = name
        sillObject.age = age
    def Func(anyThing):
        print("Hello, my name is ",anyThing.name)
    
person1 = Person("Fethi",20)
person1.Func()
# Modify object properties
person1.age = 60
print("updated age: ",person1.age)
# delete object properties by using del keyword
del person1.age
print("age property is deleted") # print("deleted age: ",person1.age) will cause an error: 'Person' object has no attribute 'age'
# delete object by using del keyword
del person1
print("person1 is deleted") # print("deleted object: ",person1) will cause an error: name 'person1' is not defined
