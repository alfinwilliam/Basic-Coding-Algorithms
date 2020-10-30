#string slicing

a = "Hello, World!"
print(a[2:5]) # 5th string value
print(a[-6:]) # till 6th char from right
print(a[-6:-2]) # value before colon is starting and after colon ending value

#str length
print(len(a))

b = " lines in beg and end for a reason  "
print(b.strip()) #strips white spaces in beginnning and end

print(b.upper())
print(b.lower())
print(b.replace("e","E")) #replaces a string with another string

b ="alfin,shanu"
x = b.split(",")
print(type(x))

x = "al" not in b
print(x)

x = "sh" in b
print(x)

x = b + b  #string concat
print(x)



# using format function we can add int values to string.

i = "alfin is a good {}"
b= "boy"
print(i.format(b))

m = "sharlet"
s = "shanu"
so = "alfin"

endstat = "Wishal consists of {} , {} , and {}"
print(endstat.format(m,s,so))

a = 1
b = 2
c = 3
order = "after {1} comes {2} then {0}"
print(order.format(c,a,b))



#use escape character in front of illegal characters in a string

print("this is \" illegal to do inside a \" string")

#string count

stre = " rrrrrrrrrrr"

print(stre.count('r'))

print(stre.islower())

#boolean.. use to evaluate an expression

# Almost any value is evaluated to True if it has some sort of content.

def myfunction():
    return True

if myfunction():
    print("YES")