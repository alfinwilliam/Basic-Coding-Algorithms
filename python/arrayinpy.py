#python doesnot have inbuilt support for arrays
# to work with arrays in python , we need to import numpy library
#array contains elements of same datatype unlike list
cars = ['bentley','merc','audi','bmw']
print(cars)
cars.append('Maruti')
print(cars)
cars.pop(2)
print(cars)
#remove only removes first instance of value
cars.remove("Maruti")
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)