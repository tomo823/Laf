# Purpose: To extract URL and title from script.log and make a dictionary file for URL

import re
import json


list = []
l = []
dict = {}

with open("script.log", "r") as f:
    s = f.read()
    #URLの抽出
    urls = re.findall(r"https://www.youtube.com/watch\?v=[a-zA-Z0-9_-]{11}", s) 
    #Titleの厳選
    for i in re.findall("【.*】", s):
        if len(i) > 10:
            l.append(i)
    f.close()

print(f"All video titles:\n{len(l)}, {l}, end='\n\n'")


#Titleの整理,listに格納
for i in range(int(len(l)/3)):
    list.append(l[3*(i)])
print(f"Arranged video tites:\n{list}, end='\n\n'")


#URLの整理
print(f"All urls:\n{len(urls)}, {urls}, end='\n\n'")


#Dict作成
for i in range(len(urls)):
    dict[urls[i]] = list[i]

#As confirmation
print(dict)
print()


"""
#Make a text file for URL
with open("URL.txt", "w") as file:
    json.dump(dict, file)"""


#Opening text file and modify it
"""f = open("URL.txt", "r")
new_dict = json.load(f)
print(new_dict)
print()
    
dict.update(new_dict)"""

print(dict)
with open("URL.txt", "a") as file:
    file.write(str(dict))


#Delete to write other logs
"""with open("script.log", "w") as file:
    pass"""