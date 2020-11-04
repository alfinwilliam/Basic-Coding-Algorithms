x = int(input("Enter a number- "))
if x%2 == 0:
    print(format(x)+" is even")
else:
    print(format(x)+" is odd")
n = int(x/2)
if x > 1:
    for i in range(2,n):
        if n%i == 0:
            print(format(x)+" is not prime")
            break
        else:
            print(format(x)+" is prime")
else:
    print(format(x)+"is not prime")

