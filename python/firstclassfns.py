def square(n):
    return n * n

def cube(x):
    return x * x * x

# here function is assigned to a variable. this is how first class variables are used in python.
# a method is a first citizen member in python
# we can assign fn to a variable , return a function and set fns as arguments to another fn

f = square
print(f(5))

def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square,[1,2,3,4,5])
cubes = my_map(cube,[1,2,3,4,5,6])
print(squares)
print(cubes)

#returning fn as output

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}><{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test headline!')
print_h1('Another headline!')


