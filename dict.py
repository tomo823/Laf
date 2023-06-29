import glob
import re


list = []
text = ""

folder_list = [
    "./movies/【高校数学1】数と式",
    "./movies/【中1数学】一次方程式",
    "./movies/【中1数学】空間図形",
    "./movies/【中1数学】正の数・負の数",
    "./movies/【中1数学】比例・反比例",
    "./movies/【中1数学】文字式",
    "./movies/【中1数学】平面図形",
    "./movies/【中2数学】一次関数",
    "./movies/【中2数学】確率",
    "./movies/【中2数学】三角形と四角形",
    "./movies/【中2数学】式の計算",
    "./movies/【中2数学】平行線・多角形・合同",
    "./movies/【中2数学】連立方程式",
    "./movies/【中2数学】連立方程式",
    "./movies/【中3数学】三平方の定理",
    "./movies/【中3数学】式の展開と因数分解",
    "./movies/【中3数学】相似な図形",
    "./movies/【中3数学】二次関数",
    "./movies/【中3数学】二次方程式",
    "./movies/【中3数学】平方根",
    "./movies/高校数学１  集合と命題",
    "./movies/資料の活用",]

"""for files in folder_list:
    path_list = glob.glob(files + "\*")
    for path in path_list:
        print(path)
        with open(path, "r") as f:
            text = f.read()
            dict[files] = text"""

"""for files in folder_list:
    path_list = glob.glob(files + "/*")
    for path in path_list:
        with open(path, "r") as f:
            text = f.read()
            dict[path] = text
    print(dict)"""

for files in folder_list:
    path_list = glob.glob(files + "/*")
    for path in path_list:
        with open(path, "r") as f:
            text = f.read()
            list.append(text)

print(list)