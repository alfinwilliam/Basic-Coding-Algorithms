thisset = {"apple","banana","cherry"}
print(thisset)

for x in thisset:
    print(x)

if "apple" in thisset:
    print("Apple present in set.")

print('apple' in thisset)

# add value to set

thisset.add("orange")
print(thisset)

thisset.add("Orange")
print(thisset)

thisset.update(["mango","grapes"])
print(thisset)

print(len(thisset))

thisset.remove("banana")
thisset.discard("grapes")

print(thisset)

#del thisset
#thisset.clear()

# Adding two sets

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

set1.update(set2)
set1.union(set2)

print(set1)

newset = set(("apple","orange","mango","mosambi"))
print(newset)