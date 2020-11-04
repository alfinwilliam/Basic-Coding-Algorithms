n=int(input("enter limit :"))
a = 0
b = 1
i = 0
print(a)
print(b)
while i<n:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1
