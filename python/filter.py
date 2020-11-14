# used to filter results - filter() fn

def evencheck(a):
    return a % 2 == 0

lst = [2,4,6,8,10,11,13,15]

evn = list(filter(evencheck,lst))

#print(evn)

# using lambda with filter fn

evn = list(filter(lambda a : a % 2 ==0,lst))
print(evn)


# using map fn for doubling the resultant list values

doublist = list(map(lambda d: d * 2,evn))
print(doublist)

# to use reduce we need to import functools

from functools import reduce

redresult = reduce(lambda b,s: b + s,doublist)

print(redresult)