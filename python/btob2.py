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