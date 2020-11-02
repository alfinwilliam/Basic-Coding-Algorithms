thistuple = ("apple","banana","cherry")
print(thistuple)

print(thistuple[-3:])

#change value tuple workaround.. change to list .. change value and then back to tuple.

tuplist = list(thistuple)
tuplist[1] = "alfin"
newtuple = tuple(tuplist)
print(newtuple)

for x in newtuple:
    print(x)

if "alfin" in newtuple:
    print("alfin exists")

print(len(newtuple))

thistuple = ("alfin",)

print(type(thistuple))

# delete tuple

#del thistuple

tuplea = (1,2,3,4)
tupleb = ("a","b","c","d")

tuplec = tuplea + tupleb
print(tuplec)

x = tuplec.count('a')
print(x)