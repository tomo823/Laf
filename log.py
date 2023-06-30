import re
import json


list = []
l = []
dict = {}

with open("script.log", "r") as f:
    s = f.read()
    #URLの抽出
    urls = re.findall(r"https://www.youtube.com/watch\?v=[a-zA-Z0-9]{11}", s) 
    #Titleの厳選
    for i in re.findall("【.*】", s):
        if len(i) > 10:
            l.append(i)
    f.close()


#Titleの整理,listに格納
for i in range(int(len(l)/3)):
    list.append(l[2*i+2])

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
f = open("URL.txt", "r")
new_dict = json.load(f)
print(new_dict)
print()
    
dict.update(new_dict)

print(dict)
with open("URL.txt", "w") as file:
    json.dump(dict, file)


#Delete to write other logs
"""with open("script.log", "w") as file:
    pass"""