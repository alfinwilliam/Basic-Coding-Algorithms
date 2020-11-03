# a, b = input().split()
# print(max(a,b), " is greatest")

# if a > b:
#     print("a is greatest")
# elif a == b:
#     print("a & b are equal")
# else:
#     print("a is greatest")

# if you have only one statement to execute , you can put in same line as if statement

# if a > b: print("a is greatest")

x, y, z = input().split()
if x>y and x>z:
    print(x+" is greatest")
elif y>z and y>x:
    print(y+" is greatest")
else:
    print(z+" is greatest")