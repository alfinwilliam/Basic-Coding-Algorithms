fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

x = "banana"
for a in x:
    print(a)

a = [1,2,3]

for x in a:
    print(x)
    if x == 2:
        break

# range function in python

# - to loop through a set of code for a specific number of time , we use range function.

# range() function returns a sequence of numbers , starting from 0 to till the specified number.

# but range(6) only returns 0 -5 since iteration starts at 0.

for x in range(6):
    print(x)

for x in range(2,6):  #starts from 2 but does not include 6
    print(x)

for x in range(2,6,3): #increments by 3
    print(x)

# Else statement at the end of for loop

for x in range(3):
    print(x)
else:
    print("now looping has finished")

adj = ["red","greeen","orange"]
fruit = ["apple","mango","mosambi","banana"]

for x in adj:
    for y in fruit:
        print(x,y)

# use pass statement for a empty for loop

for x in [1,2,3,4]:
    pass