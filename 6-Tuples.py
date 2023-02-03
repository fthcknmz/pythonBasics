print("\n****BASICS OF TUPLE****") #BASICS OF TUPLE
myTuple = ("apple","bannana","cherry")
# Tuple is one of 4 built-in data types in Python used to store collections of data,
# The other 3 are List,Set,Dictionary
# A Tuple is a colleciton which is ordered and unchangeable
# Tuples are written with round-brackets
Tuple = ("apple","bannana","cherry","apple","cherry") # allows duplicate values
print(Tuple)
print("the length of the Tuple: ",len(Tuple),"\n")
print("the type of a tuple: ",type(Tuple))
#one item Tuple
Tuple=("apple",) # remmember the comma
print(Tuple)
Tuple=("apple") # NOT a Tuple
print(Tuple,"\n")
# A Tuple can contain different data types
tuple1=("abc",35,True,44,"human")
print(tuple1,"\n")
# The tuple() constructor
thisTuple=tuple(("apple","bannana","cherry")) #NOTE the double round-brackets
print(thisTuple)

print("\n**** ACCESS TUPLES ****") # ACCESS TUPLES
thisTuple=("apple","bannana","cherry") #NOTE the double round-brackets
print(thisTuple)
print(thisTuple[1],"  (printed the second element)\n")
#negative indexing
thisTuple=("apple","bannana","cherry")
print(thisTuple)
print(thisTuple[-1],"  (-1 refers to the last element)\n")
#range of indexes
thisTuple=("apple","bannana","cherry","watermelon","kiwi","orange","melon","mango")
print(thisTuple)
print(thisTuple[2:5],"  (printed from the 2nd element to the 4th element)\n")
#range of indexes
thisTuple=("apple","bannana","cherry","watermelon","kiwi","orange","melon","mango")
print(thisTuple)
print(thisTuple[2:],"  (printed from the 2nd element to the last element)\n")
#range of negative indexes
thisTuple=("apple","bannana","cherry","watermelon","kiwi","orange","melon","mango")
print(thisTuple)
print(thisTuple[-4:-1],"  (printed from the -4th element to the -1th element)\n")
# check if item exists
thisTuple=("apple","bannana","cherry","watermelon","kiwi","orange","melon","mango")
if "apple" in thisTuple:
    print("Yes, 'apple' is in the box")

print("\n**** UPDATE TUPLES ****") # UPDATE TUPLES
#once a Tuple is created, you cannot change its values.
#but there is a workaround
thisTuple=("apple","bannana","cherry")
print(thisTuple)
thisList=list(thisTuple)
thisList[1]="kiwi"
thisTuple=tuple(thisList)
print(thisTuple,"\n")
#once a tuple is created, you cannot add items to it
# thisTuple.append("orange") raises an error
#but again there is a workaround
thisTuple=("apple","bannana","cherry")
print(thisTuple)
thisList=list(thisTuple)
thisList.append("orange")
thisTuple=tuple(thisList)
print(thisTuple,"\n")
#once a tuple is created, you cannot remove items from it
#but again there is the same workaround.
thisTuple=("apple","bannana","cherry")
print(thisTuple)
thisList=list(thisTuple)
thisList.remove("apple")
thisTuple=tuple(thisList)
print(thisTuple,"\n")
#we can delete a Tuple completely
thisTuple=("apple","bannana","cherry")
print(thisTuple)
del thisTuple
print("the Tuple is deleted") # print(thisTuple) raises NameError  --name 'thisTuple' is not defined--

print("\n**** UNPACK TUPLES ****") # UNPACK TUPLES
# in Python, we are allowed to extract the values back into variables
thisTuple=("apple","bannana","cherry")
(green, yellow, red) = thisTuple #unpacking
print("green: ",green)
print("yellow: ",yellow)
print("red: ",red)
print()
#using asterix(*)
thisTuple=("apple","bannana","cherry","strawberry","raspberry")
(green, yellow, *red) = thisTuple #unpacking with asterix(*)
print("green: ",green)
print("yellow: ",yellow)
print("red: ",red)
print()
thisTuple=("apple","bannana","cherry","strawberry","raspberry")
(green, *yellow, red) = thisTuple #unpacking with asterix(*)
print("green: ",green)
print("yellow: ",yellow)
print("red: ",red)

print("\n**** LOOP TUPLES ****") # LOOP TUPLES
#looping by using for
thisTuple=("apple","bannana","cherry")
for x in thisTuple:
    print(x)
print() 
# or we can loop the index numbers
thisTuple=("apple","bannana","cherry")
for i in range(len(thisTuple)):
    print(thisTuple[i])
print()
#looping by using while
thisTuple=("apple","bannana","cherry")
i=0
while i < len(thisTuple):
    print(thisTuple[i])
    i=i+1

print("\n**** JOIN TUPLES ****") # JOIN TUPLES
tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3,"\n")
# multiply Tuples
fruits=("apple","bannana","cherry")
thisTuple=fruits*2
print(thisTuple)

print("\n**** TUPLE METHODS ****") # TUPLE METHODS
fruits=("apple","bannana","cherry")
thisTuple=fruits*2
print(thisTuple.count("apple")) #returns how many times apple occurs in the list
print(thisTuple.index("cherry",0,6)) # searches the Tuple and finds "cherry" and returns the position of where it is found