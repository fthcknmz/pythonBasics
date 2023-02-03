# wihle loop
i=1
while i<6:
    print(i)
    i += 1 # same as i = i + 1
print()
# break statement
i=1
while i<6:
    print(i)
    if(i == 4):
        break
    i += 1 # same as i = i + 1
print()
# continue statement
i=1
while i<6:
    if(i == 4):
        continue # continue to next iteration if i is 3
    print(i)
    i += 1 # same as i = i + 1
print()
# else statement
i=1
while i<6:
    print(i)
    i += 1 # same as i = i + 1
else:
    print("i is no longer less than 6")