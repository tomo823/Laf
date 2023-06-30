import re


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

#Titleの整理,listに格納
for i in range(int(len(l)/3)):
    list.append(l[2*i+2])

for i in range(len(urls)):
    dict[urls[i]] = list[i]

print(dict)

"""with open("script.log", "w") as file:
    pass"""