# python lists

#list is a collection ie ordered and interchangeble. Allows duplicate members
#Tuple is a collection ie ordered and unchangeble. Allows duplicate members
#Set is a collection ie unordered and unindexed. No duplicate members.
#Dictionary is a collection ie unordered, changeble and indexed. No duplicate members.

# new update : tomorrow second envestnet test. 5 candidates. one position.

# list is a collection ie ordered , indexed and contains duplicate values

thislist = [2,4,6,8,9,10,11,13,14,16,18]
print(thislist[2])

print(thislist[2:3])
print(thislist[2:])
print(thislist[:9])

# for x in thislist:
#     print(x)

if 9 in thislist:
    print("nine is in this list")

print(len(thislist))

thislist.append(20) #adds to end of list
print(thislist)

thislist.insert(1,5) #index,value insert
print(thislist)

thislist.remove(5) #removes specified value
print(thislist)

thislist.pop() #deletes value at end of list

thislist.pop(3) #deletes value in specific index
print(thislist)

del thislist[0] #deletes value in specific index
print(thislist)

#del thislist   < removes list completely.  

#thislist.clear() # removes entire content of list
print(thislist)

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)


for x in mylist:
    thislist.append(x)

print(thislist)

newlist = thislist + mylist
print(newlist)

newlist.extend(thislist)
print(newlist)

famlist = list(("alfin","shanu","sharlet"))
print(famlist)