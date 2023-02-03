Set={"apple","bannana","cherry"}
print(Set)
# sets are used to store multiple items in a single variable
# Set is one of 4 built-in data types in a single variable
# A set is a collection which is both unordered and unindexed
# sets are written with curly brackets
print("\n****SET BASICS****") # **** SET BASICS ****
#duplicate will be ignored, sets cannot have two items with the same value
Set={"apple","bannana","cherry","apple"}
print(Set)
print("length of the set: ",len(Set))
#set can contain different data types
set1={"apple",34,True,44}
print(set1)
Set={"apple","bannana","cherry","apple"}
print("the type of set: ",type(Set))
thisSet= set(("apple","bannana","cherry")) # NOTE the double roun-brackets
print(thisSet)

print("\n****ACCESS SET ITEMS****") # **** ACCESS SET ITEMS ****
Set={"apple","bannana","cherry"}
for x in Set:
    print(x)
print()
#check if "bannana" is present in the list
Set={"apple","bannana","cherry"}
print("is 'bannana present': ","bannana" in Set)

print("\n****ADD SET ITEMS****") # **** ADD SET ITEMS ****
# using add() method
Set={"apple","bannana","cherry"}
Set.add("orange")
print(Set)
# another way is update() method 
Set={"apple","bannana","cherry"}
tropical={"pineapple","mango","papaya"}
Set.update(tropical)
print(Set)
#add any iterable
Set={"apple","bannana","cherry"}
List=["kiwi","orange"]
Set.update(List)
print(Set)

print("\n****REMOVE SET ITEMS****") # **** REMOVE SET ITEMS****
Set={"apple","bannana","cherry"}
Set.remove("bannana") # if th item to remove doesnt exist, remove() will raise an error
print(Set)
# remove 'bannnana' by using discard() method
thisSet={"apple","bannana","cherry"}
thisSet.discard("bannana") #if th item to remove doesnt exist, discard() will NOT raise an error
print(thisSet)
# pop() method also can be used
Set={"apple","bannana","cherry"}
x = Set.pop()  # we dont know which item that gets removed (Sets are unordered)
print("x: ",x)
print("Set: ",Set)
# The clear() method empities the set
Set={"apple","bannana","cherry"}
Set.clear()
print(Set,"  -set is cleared")
# The del keyword will delete the set completely 
Set={"apple","bannana","cherry"}
del Set
print("set is deleted") #print(Set) will raise an error

print("\n****LOOP SETS****") # **** LOOP SETS ****
Set={"apple","bannana","cherry"}
for x in Set:
    print(x)

print("\n****JOIN SETS****") # **** JOIN SETS ****
# The union() method returns a new set with  all items from both sides
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)
print()
# The update() method inserts items in set2 into set1
set1={"a","b","c"}
set2={1,2,3}
print(set1)
set1.update(set2)
print(set1)
print()
# keep only the duplicates
x={"apple","bannana","cherry"}
y={"apple","google","microsoft"}
x.intersection_update(y) # will keep only the items that are present in both sets
print(x)
print()
# intersection() method will return a new set that only contains the items present in both sets
x={"apple","bannana","cherry"}
y={"apple","google","microsoft"}
z=x.intersection(y)
print(z)
print()
# keep all but not the duplicates
x={"apple","bannana","cherry"}
y={"apple","google","microsoft"}
x.symmetric_difference_update(y) # keeps items not present in both sets
print(x)
print()
# symmetric_difference() method will return a new set that contains only the elements that are not present in both sets
x={"apple","bannana","cherry"}
y={"apple","google","microsoft"}
z=x.symmetric_difference(y) # keeps items not present in both sets
print(z)
print()