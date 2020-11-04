x,y,z = input("Enter three numbers -").split()
if(x>y and x>z):
    print(format(x)+" is largest")
elif(y>x and y>z):
    print(format(y)+" is largest")
else:
    print(format(z)+" is largest")