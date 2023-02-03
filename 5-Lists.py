print("\n****LISTS BASICS****") #LIST BASICS
# Lists are used to store multiple items in a single variable.
List=["apple","bannana","cherry"]
print(List)
# Since lists are indexed, lists can have items with the same value.
List=["apple","bannana","cherry","apple","cherry"]
print(List)
List=["apple","bannana","cherry"]
print("list length: ", len(List))
# A list can contain different data types
List1=["abc",34,False,44,"astounding"]
print(List1,"   (List with different data types)")
# in Python, Lists are defined as objects with the data type 'list'
List=["apple","bannana","cherry"]
print(type(List))
# list can be used to create a new  list
thisList = list(("cat","dog","mice")) # note the duoble round-brackets
print(thisList)

print("\n****ACCESS LIST ITEMS****") #ACCESS LIST ITEMS
List=["apple","bannana","kiwi","orange","mango","cherry"]
print(List[1]) #will print bannana
#-1 refers to the last item
print(List[-1]) #will print cherry 
#range of indexes
print(List[2:5])
#from the start to 3th element
print(List[:4])
#from 4th element to the end
print(List[4:])
#range of negative indexes
print(List[-4:-1])
#Check if 'apple' exist in the list
if "apple" in List:
    print("Yeah, apple is in the box")

print("\n****CHANGE LIST ITEMS****") #CHANGE LIST ITEMS
List=["apple","bannana","kiwi","orange","mango","cherry"]
print(List)
List[1]="blackcurrant"
print(List)
#change a range of ıtem values
List[1:4]=["blackcurrant","watermelon","blackberry"]
print(List)
List[1:4]=["watermelon"] # the items will be inserted.
print(List)
#insert items
List.insert(2,"watermelon") # inserts a new item without replacing any of the existing values
print(List)

print("\n****ADD LIST ITEMS****") #ADD LIST ITEMS
# append items
List=["apple","bannana","cherry"]
print(List)
List.append("orange") # adds an item to the end of the list
print(List,"\n")
#insert items
List=["apple","bannana","cherry"]
print(List)
List.insert(1,"orange") # adds an item as the second position 
print(List,"\n")
#extend list
List=["apple","bannana","cherry"]
Tropical=["mango","pineapple","papaya"]
print(List)
List.extend(Tropical) # adds the elements to the first List
print(List,"\n")
#Add any iterable: extend() can add any iterable objects (tuples,sets,dictionaries)
List=["apple","bannana","cherry"]
Tuple=("kiwi","orange")
print(List)
List.extend(Tuple) # adds the elements to the first List
print(List)

print("\n****REMOVE LIST ITEMS****") #REMOVE LIST ITEMS
#remove specific item
List=["apple","bannana","cherry"]
print(List)
List.remove("bannana")
print(List,"\n")
#remove specified index
List=["apple","bannana","cherry"]
print(List)
List.pop(1) # if you don not specify the index, pop() removes the last item 
print(List,"\n")
#del keyword also deletes the list completely
List=["apple","bannana","cherry"]
print(List)
del List
print("the list is deleted\n") # print(List,"\n") gives error because there is no List anymore
#clear the list
List=["apple","bannana","cherry"]
print(List)
List.clear() # clears the contents
print(List,"\n")

print("\n****LOOP LISTS****") #LOOP LISTS
#using 'for' loop
thisList=["apple","bannana","cherry"]
for i in range(len(thisList)): # use range() and len() to create a suitable iterable
    print(thisList[i])
print()
#using 'while' loop
thisList=["apple","bannana","cherry"]
i=0
while i < len(thisList):
    print(thisList[i])
    i=i+1
print()
#using list comprehension
thisList=["apple","bannana","cherry"]
[print(x) for x in thisList]

print("\n****LIST COMPREHENSION****") #LIST COMPREHENSION
fruits = ["apple","bannana","cherry","kiwi","mango"]
newList = []
for x in fruits:
    if "a" in x:  # we want only the fruits containing the letter "a"
        newList.append(x)
print(newList,"\n")

#we can do that with only one line of code
fruits = ["apple","bannana","cherry","kiwi","mango"]
newList = [x for x in fruits if "a" in x]
#The syntax: newList = [expression for item in iterable if condition == True]
print(newList)

print("\n****SORT LISTS****") #SORT LISTS
# Sort list alphanumerically
thisList = ["apple","cherry","kiwi","mango","bannana"]
print(thisList)
thisList.sort()
print(thisList,"    --Sort list alphanumerically\n")
# Sort list numerically
thisList = [100,50,55,69,34,2]
print(thisList)
thisList.sort()
print(thisList,"    --Sort list numerically \n")
# Sort descending
thisList = [50,100,55,69,34,2]
print(thisList)
thisList.sort(reverse = True)
print(thisList,"    --Sort descending\n")
# Custumize sort function
thisList = [50,100,55,69,34,2]
print(thisList)
def thisFunc(n):
    return abs(n-50) #sort the list based on how close the number is to 50
thisList.sort(key = thisFunc)
print(thisList,"    --Custumize sort function\n")
# Case Insensitive Sort
thisList = ["apple","Orange","cherry","kiwi","mango","bannana"]
thisList.sort()
print(thisList,"    --sort() is case sensitive\n")
thisList.sort(key = str.lower)
print(thisList,"    --we can use built-in functions as key functions when sorting a list\n")
# Reverse Order
thisList = ["apple","cherry","kiwi","mango","bannana"]
print(thisList)
thisList.reverse()
print(thisList,"    --Reverse Order\n")

print("\n****COPY A LIST****") #COPY A LIST
#use built-in list method copy()
thisList = ["apple","bannana","cherry"]
myList = thisList.copy()
print(myList)
#use built-in list method list()
thisList = ["apple","bannana","cherry"]
myList = list(thisList)
print(myList)

print("\n****JOIN LIST****") #JOIN LIST
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3,"\n")
# another way
list1=["a","b","c"]
list2=[1,2,3]
for x in list2:
    list1.append(x)
print(list1,"\n")
# another way
list1=["a","b","c"]
list2=[1,2,3]

list1.extend(list2)
print(list1)