def myfn():
    return True

if myfn():
    print("YES")
else:
    print("No")


# python isinstance.. to check whether same datatype

x = 200
print(isinstance(x, int))

#python Operators

# 1. Arithmetic Operators

#arithmetic operators are used with numeric values to perform common mathematical operations

print(2+3) #addition
print(3-2) #subtraction
print(2*3) #multiplication
print(2/3) #division
print(3%2) #modulus
print(3**2) #exponentiation
print(3 // 2) #floor division

# 2. Assignment Operators

#assignment operators are used to assign values to variables.

x = 5
x += 3
x -= 3
x *= 3
x /= 3
x **= 3
x//= 3
x %= 3
x &= 3
x |= 3
x ^= 3
x >>= 3
x <<= 3

#seems a little tough , I'll come back to the less known ones later - on pratical sessions

# 3. Comparison Operators

#used to compare two values

x = 5
y = 2
x == y # used to check equality

x != y # not equal to
x > y #greater than
x < y #less than
x >= y #greater than or equal to
x <= y #less than or equal to

# 4. Logical Operators

# used to combine conditional statements

if x > 5 and x < 10:  # returns true if both statements are true
    print("True")

if x < 5 or x < 4: #returns true if any one of the statement is true
    print("True")

if not(x < 5 and x> 4):  #reverses result.. false if the condition is true.
    print("This is how not works")


# 5. python identity operators

#used to compare objects , not if they are equal , but if they are same objects with same memory location.

if ( x is y):
    a = ({} is {})
    print(a.format(x,y))

# is .. returns true if both variables are same object

if ( x is not y):
    a = ({} is not {})
    print(a.format(x,y))

# is not.. returns true if both variable are not same object

# 6. Python Membership operator ( just like a club membership)

x in y # returns true if value of x is present in y
x not in y # returns true if value of x is not present in y


# 6. Bitwise Operator

#bitwise operators used to compare binary numbers
# I'll come back to this later after learning the essential stuff.





