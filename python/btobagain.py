print("Hello World")
# single line comment
"""
this is a 
multiline comment
"""
print(5 > 2)
print("alfin" + "william")
print("alfin" * 2)

x = 5
y = "John"

print(x)
print(y)

x = 5
x = 'sally'
# now datatype of x is str

x = 'John'
x = "John"

x, y, z = 'alfin','shanu','sharlet'
print(x+' '+y+' '+z)

x = "alfin"

print("ippo bodhodhayam vannu " +x+" inu")

#global variables

x = "awesome"

def myfunc():
    #local variable x
    x = "fantastic"
    #creating a global variable y inside function
    global y 
    y = "bomblastic"
    print("python is "+x)
    print("python is also "+y)

myfunc()

#change value of global variable inside function

def valuefun():
    global x
    x = "new value inside function"
    print("Global variable x value is "+x)

valuefun()

y = 14.5
print(type(y))

# converting number datatypes using constructor fns

x = 12
y = 15.6
z = 3+8j

print( float(x) )
print( int(y) )
print( complex(x) )

#random module to get a random value

import random

for i in range(10):
    print(random.randrange(1,10))