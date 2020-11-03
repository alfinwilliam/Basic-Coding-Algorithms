thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

thisdict["year"] = 1997

print(thisdict["year"])

# to print keys in dict

for x in thisdict:
    print(x)

# to print values in dict

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x,y in thisdict.items():
    print(x,y)

print(type(x))

thisdict["color"] = "red"

print(thisdict["color"])

for x,y in thisdict.items():
    print(x,y) 

#removing a value from dict

thisdict.pop("model")

del thisdict["color"]

#del thisdict

#thisdict.clear()
