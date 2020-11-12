#lambda function is small anonymous function

#lambda function can take any number of arguments , but only have one expression

x = lambda a : a + 10

# here a is the argument and the portion after colon is expression

print(x(5))

x = lambda a, b : a * b

print(x(5,2))

x = lambda a, b, c : a + b + c

print(x(2, 3, 4))

# lambda mostly used as anonymous function inside a fn definition

def myfn(n):
    return lambda n: 2 * n


myfn(2)

modvalue = lambda a, b : a % b

print(modvalue(31, 5))