#two primitive loop commands.. while and for

a = 1 
sum = 0
while(a<10):
    sum = sum + a
    a = a + 1
print(sum)

#using break statement

a = 1
while(a<6):
    print(a)
    if(a == 3):
        break
    a+=1

#using continue statement

a = 1
while(a<6):
    a+=1
    if(a == 3):
        continue
    print(a)
