test_str = input()
print("The original string is : " + str(test_str)) 
res = ''.join(format(ord(i), 'b') for i in test_str) 
print("The string after binary conversion : " + str(res)) 
