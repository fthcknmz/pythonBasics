# if statement
a = 133
b = 55
if a>b:
    print("a is greater than b")
"""
Pyhton relies on identation (whitespace at the beginning of a line)
so, following syntax will raise an error
if a>b:
print("a is greater than b")
"""
# elif keyword represents else if
a = 55
b = 55
if a>b:
    print("a is greater than b")
elif a==b:
    print("a equals b")
# else keyword represents else
a = 55
b = 100
if a>b:
    print("a is greater than b")
elif a==b:
    print("a equals b")
else:
     print("b is greater than a")
print()
# Short hand if
a = 122
b = 1
if a > b:  print("a is greater than b")
# Short hand if...else
a = 2
b = 100
print("a is greater than b") if a>b else print("a is not greater than b")
# Short hand if...elif....else
a = 2
b = 2
print("a is greater than b") if a>b else print("b is greater than a") if b>a else print("a equals b")
print()
#And
a = 200
b = 2
c = 2000
if a>b and a<c:
    print("both conditions are true")
#Or
a = 200
b = 2
c = 2000
if a>b or a<c:
    print("At least one of the conditions is true")
print()
#Nested if
x = 19
if x > 10:
    print("above 10,")
    if x > 20:
        print("above 20\n")
    else:
        print("But not above 20\n")