print("\n***STRINGS ARE ARRAYS***") #STRINGS ARE ARRAYS
a = "Hello, World!"
print(a[0])

print("\n***LOOPING THROUGH A STRING***") #LOOPING THROUGH A STRING
for x in "Hello":
    print(x)
    
print("\n***STRING LENGTH**") #STRING LENGTH
a = "Hello, World!"
print('length of a: ',len(a)) # len() function returns the length of a string

print("\n***CHECK STRING***") #CHECK STRING
txt="Freedom is everything in the life"
print("everything" in txt) # check if "everything" is present in txt (will be true)
print("expensive" not in txt) # check if "expensive" is not present in txt (will be true)


if "everything" in txt:
    print("Yeah,'everything' is present in txt.")
if "expensive" not in txt:
    print("Yeah,'expensive' is not present in txt.")

print("\n***SLICING STRINGS***") #SLICING STRINGS
a = "Hello, World!"
print(a)
print(a[1:5]) # slice from 1 to 5
print(a[:10]) # slice from the start to 10
print(a[5:]) # slice from 5 to the end
print(a[-5:-2]) # use negative indexes to start the slice from the end of the string

print("\n***MODIFY STRINGS***") #MODIFY STRINGS
a = "  Hello, World!  "
print(a)
print(a.upper()) # upper() returns the string in upper case
print(a.lower()) # lower() returns the string in upper case
print(a.strip()) # strip() removes whitespaces before or after the actual text

print("\n***REPLACE STRING***") #REPLACE STRING
a = "Hey! Hello, World!"
print(a.replace("H", "J")) # replaces H's with J's

print("\n***SPLIT STRING***") #SPLIT STRING
a = "Hello, World!"
print(a.split(",")) # split() splits the string at , separator

print("\n***STRING FORMAT***") #STRING FORMAT
age = 20
txt = "My name is Fethi, and i am {}"
print(txt.format(age)) # format() takes age formats it and places it in the string where {} is

#Another example
quantity=5
itemno=3350
price=50.49
order="I want to order item {1} for {0} of them which is {2} dollar for each."
print(order.format(quantity,itemno,price))

print("\n***ESCAPE(\) CHARACTER***") #ESCAPE(\) CHARACTER
# To insert characters that are illegal in a string, use escape character(\)
txt="We are the so-called \"Vikings\" from the north." #"We are the so-called "Vikings" from the north." causes an error
print(txt)


