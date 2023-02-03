# Lists, Tuples, Dictionaries, and Sets are all iterable objects.
# All these objects have a iter() method wihch is used to get an iterator
myTuple = {"apple","bannana","cherry"}
myIterator = iter(myTuple)
print("1st iteration:",next(myIterator))
print("2nd iteration:",next(myIterator))
print("3rd iteration:",next(myIterator))
print()
#Strings are also iterable objects
myString = "Hello"
myIterator = iter(myString)
print("1st iteration:",next(myIterator))
print("2nd iteration:",next(myIterator))
print("3rd iteration:",next(myIterator))
print("4th iteration:",next(myIterator))
print("5th iteration:",next(myIterator))
print()
# Looping through an iterator
myTuple = {"apple","bannana","cherry"}
for x in myTuple:
    print(x)
# iterate the characters of a string
myString = "Hello"
for x in myString:
    print(x)
print()
# To creaate an object/class as an iterator we have to implement the methods __iter__() and __next__() to our object
# All classes have a function called __init__(), which allows us to do some initializing when the object is being created
# __iter__() methods acts similar.
class myNumbers:
    def __iter__(self):
        self.a = 1  # starting with 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1 # and each sequance will increase by 1
        return x
myClass = myNumbers()
myIter = iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

# to prevent the iteration to go on forever (in for loop for example), we can use the StopIteration statement.
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
myClass = myNumbers()
myIter = iter(myClass)
for x in myIter:
    print(x)
