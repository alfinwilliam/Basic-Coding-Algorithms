import re 
ini_str = input()
print ("Initial String", ini_str) 
res_list = [] 
res_list = re.findall('[A-Z][^A-Z]*', ini_str) 
print("Resultant prefix", str(res_list)) 
