Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
print(Dictionary,"\n")
# A dictionary is a collection which is unordered,changeable and does not allow duplicates.
# Dictionaries are written with curly-brackets and have keys and values
print("\n**** DICTIONARY BASICS ****") # **** DICTIONARY BASICS ****
# Duplicate values will be overwrite existing values
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2021
    }
print(Dictionary,"\n")
print("length of the dictionary: ",len(Dictionary),"\n")
print("type of the dictionary: ",type(Dictionary))

print("\n**** ACCESS DICTIONARY ITEMS ****") # **** ACCESS DICTIONARY ITEMS ****
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x=Dictionary["model"]
print(x,"\n")
# get() will give the same result
x=Dictionary.get("model")
print(x,"\n")
# keys() meyhod will return a list of all the keys in dictionary
x=Dictionary.keys()
print("keys in the dictionary: ",x)
# add a new item to the original dictionary and see that the value list gets updated as well
Car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x=Car.keys()
print("\nbefore the change: ",x)
Car["color"]="red"
print("after the change: ",x)
# values() will return a list of all values in the dictionary
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = Dictionary.values()
print("\nAll values in the dictionary: ",x)
# Add a new value item to the original dictionary
Car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x=Car.values()
print("\nbefore the change: ",x)
Car["year"]=2021
print("after the change: ",x)
# items() will return each item in a dict, as tuples in a list
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x=Dictionary.items()
print("\nitems: ",x)
# Check if key exist
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
if "model" in Dictionary:
    print("Yeah, 'model' is on of the keys")

print("\n**** CHANGE DICTIONARY ITEMS ****") # **** CHANGE DICTIONARY ITEMS  ****
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary["year"]=2021
print(Dictionary["year"],"  (it was 1964)")
# update() will update the dictionary with the items feom given argument.
# the argument must be a dictionaryi or an iterable object with key-value pairs
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary.update({"year": 2020})
print(Dictionary["year"],"  updated")

print("\n**** ADD DICTIONARY ITEMS  ****") # **** ADD DICTIONARY ITEMS  ****
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary["color"]="red"
print(Dictionary, "  -color key is added")
# update() will update the dictionary with the items from a given argument
# the argument must be a dictionary, or an iterable object with key-value pairs
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary.update({"color": "red"})
print(Dictionary)

print("\n**** REMOVE DICTIONARY ITEMS  ****") # **** REMOVE DICTIONARY ITEMS ****
# the pop() method removes the item with the specific key name
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary.pop("model")
print(Dictionary,"\n")
# popitem() removes the last inseted item
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary.popitem()
print(Dictionary.items() ,"  (year is deleted)")
# del keyword removes the item with specific key name
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
del Dictionary["model"]
print("\n",Dictionary)
# del keyword can also delete the dictionary completely
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
del Dictionary
print("Dictionary is deleted\n") #print(Dictionary) will raise an error  --name 'Dictionary' is not defined--
# clear() empities the dictionary
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
Dictionary.clear()
print(Dictionary)

print("\n**** LOOP DICTIONARIES ****") # **** LOOP DICTIONARIES ****
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in Dictionary:
    print(x)
print()
# print all values, one by one
for x in Dictionary:
    print(Dictionary[x])
print()
# values() returns all values of a dict
for x in Dictionary.values():
    print(x)
print()
# keys() returns the keys of a dict
for x in Dictionary.keys():
    print(x)
print()
#Loop through both keys and values, by using items() method
for x,y in Dictionary.items():
    print(x,y)

print("\n**** COPY DICTIONARIES ****") # **** COPY DICTIONARIES ****
# using copy() method
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
NewDictionary=Dictionary.copy()
print(NewDictionary,"\n")
# another way is to use the built-in function dict()
Dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
NewDictionary=dict(Dictionary)
print(NewDictionary)

print("\n**** NESTED DICTIONARIES ****") # **** NESTED DICTIONARIES ****
myFamily={
    "child1": {
        "name": "Emily",
        "year": 2003
        },
     "child2": {
        "name": "Adem",
        "year": 1997
        },
      "child3": {
        "name": "Hannah",
        "year": 1992
        }
    }
print(myFamily)
print()
# or 
child1 = {
        "name": "Emily",
        "year": 2003
        }
child2 = {
        "name": "Adem",
        "year": 1997
        }
child3 = {
        "name": "Hannah",
        "year": 1992
        }
myFamily= {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
   }
print(myFamily)
      