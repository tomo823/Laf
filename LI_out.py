from pathlib import Path
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor,SimpleDirectoryReader
from langchain.chat_models import ChatOpenAI
import os

import re, glob

from typing import List
from llama_index.data_structs.node_v2 import DocumentRelationship
from llama_index.response.schema import RESPONSE_TYPE
from llama_index import Document
from llama_index.response import notebook_utils


os.environ["OPENAI_API_KEY"] = '<API-KEY>'


llm_predictor = LLMPredictor(
    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
)

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


for folder in folder_list:
    documents = SimpleDirectoryReader(folder).load_data()

loaded_index = GPTSimpleVectorIndex.load_from_disk('index.json')
query = input("質問を入力してください：")
response = loaded_index.query(query)
print(response)


for node in response.source_nodes:
    if node.node.extra_info is not None:
        if "file_name" in node.node.extra_info:
            print(node.node.extra_info["file_name"])
    print(node.node.node_info)
    if node.score is not None:
        print(node.score)
    print(node.node.text)


dict = {}
text = ""

"""for files in folder_list:
    path_list = glob.glob(files + "/*")
    for path in path_list:
        with open(path, "r") as f:
            text = f.read()
            if re.match(text, response.source_nodes[0].node.text):
                dict[path] = text"""

"""for key in dict.keys():
    key = re.sub(r'.*/', '', key)
    print(key)"""


