# Python program to read 
# json file 
  
  
import json 
  
# Opening JSON file 
f = open('facevmg.json',) 
  
# returns JSON object as  
# a dictionary 
sourcedata = json.load(f) 
  
# {'https://www.facebook.com/profile.php?id=100010339921780': '0326212594'}
# print(sourcedata["https://www.facebook.com/profile.php?id=100010339921780"])