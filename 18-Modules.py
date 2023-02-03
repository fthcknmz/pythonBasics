# To create a module just save the code you want in a file with the file extensiın .py
import myModule
myModule.greeting("Fethi")
# Variables in module
import myModule2
a = myModule2.person1["age"] # access to person1 dictionary
print(a)
# re-naming a module
import myModule2 as newName # create an alias when you import a module, by using as keyword
a = newName.person1["age"]
print(a)
# Built-in modules
import platform
x = platform.system()
print(x)
print()
# there is a built in func to list all the function names (or variable names) in a module
import platform
x = dir(platform)
print(x)
print()
# You can choose to import only parts from a module, by using from keyword
from myModule3 import person1 # import only person1 from the module
print(person1["age"])