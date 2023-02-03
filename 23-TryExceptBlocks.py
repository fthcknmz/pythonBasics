# The try block lets you test a block of code for errors
# The except blocks lets you handle the error
# The finally blocks lets you execute code, regardless of the result of the try-except blocks
try:
    print(x) # will raise NameError
except NameError:
    print("Variable x is not defined")
except: # many except can be used
    print("Something went wrong")
print()
# if no error will raised
x ="hello"
try:
    print(x) # will raise NameError
except NameError:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print()
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x) # will raise NameError
except NameError:
    print("Variable x is not defined")
finally:
    print("The try-except is finished")
print()
# This can be useful to close object and clean up resources
try:
    f = open("file.txt")
    f.write("Is there a file")
except:
    print("something went wrong")
finally:
    pass
    # f.close() will raise an error because there is not such a file
print()
#Raise an exception
x = -1
if x < 0:
    raise Exception("no numbers can be below zero") # raise keyword is used to raise an exception
print()

# x="hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")