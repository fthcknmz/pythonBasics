#For loops
fruits = ["apple","bannana","cherry"]
for x in fruits:
    print(x)
print()
# Looping through a string
for x in "bannana":
    print(x)
print()
# break statement
fruits = ["apple","bannana","cherry"]
for x in fruits:
    print(x)
    if x=="bannana":
        break
print()
# continue statement
fruits = ["apple","bannana","cherry"]
for x in fruits:
    if x=="bannana":
        continue
    print(x)
print()
# the range() function
for x in range(6): 
    print(x)
print()
# the range() function, using start parameter
for x in range(2,6): 
    print(x)
print()
# the range() function, using start parameter and increament parameter
for x in range(2,30,3): 
    print(x)
print()
# else in for loop
for x in range(6): 
    print(x)
else:
    print("Finished")
print()
# break in for loop
for x in range(6): 
    if x == 3: break
    print(x)
else:
    print("Finished")
print()
# Nested loops
adj=["red","big","tasty"]
fruits=["apple","bannana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)