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