# Create a parrent class
class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
    def printAll(self):
        print("My name is",self.name,self.lastname)
person1=Person("Joe", "Köhler")
person1.printAll()

# Create a child class
class Student(Person): # will inherit the properties and methods from the Parent class
    pass # when we dont want to add any other properties or methods
student1=Student("Mark", "Köhler")
student1.printAll()

# Add properties
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self, fname, lname) # keep the inheritance of parent's __init__() func.
student1=Student("Mark", "Köhler")
student1.printAll()

# use the super() function
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # will make the childe class inherit all the methods and properties from its parent
student1=Student("Mark", "Köhler")
student1.printAll()

# Add properties
class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname) # will make the childe class inherit all the methods and properties from its parent
        self.age = age
student1=Student("Mark", "Köhler", 25)
print("age property is added: ",student1.age)

# Add methods
class Student(Person):
    def __init__(self,fname,lname,age):
        super().__init__(fname, lname)
        self.age = age
    def sayHi(self):
        print("Hi, my name is",self.name,"and i am",self.age)
student1=Student("Mark", "Köhler", 25)
student1.sayHi()

        
