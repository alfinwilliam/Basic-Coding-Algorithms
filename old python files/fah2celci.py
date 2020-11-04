import sys
print("Fahrenheit to Celcius , 1")
print("Celcius to Fahrenheit , 2")
c = int(input())
if c!=1 and c!=2:
    print("invalid input")
    sys.exit()
v = float(input("Enter value:"))
if c == 1:
    print(((v - 32.0) * 5.0 / 9.0))
if c == 2:
    print(((v * 9.0) / 5.0 + 32.0))