import re


list = []
l = []
dict = {}

with open("script.log", "r") as f:
    s = f.read()
    #URLの抽出
    urls = re.findall(r"https://www.youtube.com/watch\?v=", s)
    l = re.findall("【.*】", s)
    for i in l:
        if len(i) > 10:
            list.append(i)

print(list)
print(urls)

"""with open("script.log", "w") as file:
    pass"""