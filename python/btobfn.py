# fn is a block of code that contains arguments and return values. They are useful for code modularity and reusability
# also good for error finding.
# you can pass data as parameters to a function. It can also return data as a result.

def sum(a,b):
    s = a + b
    return s

print(sum(7,2))


def fnname(firstname,lastname):
    print(firstname+" "+lastname)

fnname("alfin","william")

#arbitary arguments , if you dont know how much arguments beforehand

def myfn(*toys):
    print(toys)

myfn("bat","ball","pen","pencil")

#keyword arguments , fn arguments as key value pair

def my_fn(child3, child2, child1):
    print("the youngest child is "+ child3)

my_fn(child1 = "renu", child2 = "data", child3 = "alfin")

#default parameter value

def my_fn(country = "norway"):
    print("I'm from "+country)

my_fn("India")
my_fn()
my_fn("sweden")