import os
import logging
import sys
import pinecone
import glob
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai
import json


import re


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
    "./movies/資料の活用"]


list = []

for files in folder_list:
    path_list = glob.glob(files + "/*")
    for path in path_list:
        with open(path, "r") as f:
            text = f.read()
            list.append(text)


os.environ["OPENAI_API_KEY"] = <OPENAI-API-KEY>
openai.api_key = <OPENAI-API-KEY>


"""logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)"""


api_key = <PINECONE-API-KEY>
pinecone.init(api_key=api_key, environment="us-west4-gcp-free", pod_type="starter")


pinecone.describe_index("keyword-search")

pinecone_index = pinecone.Index('keyword-search')


#vector取得用
vector_store = PineconeVectorStore(pinecone_index=pinecone.Index("keyword-search"))


documents = []
for folder in folder_list:
    #folderには各Directoryが入っている
    #1個1個のDirectoryの中身をdocumentsに入れている
    #documentsはlist型
    document = SimpleDirectoryReader(folder).load_data()
    documents.extend(document)


storage_context = StorageContext.from_defaults(vector_store=vector_store)


#pineconeからindexを取得
index = VectorStoreIndex.from_vector_store(vector_store)


query_engine = index.as_query_engine(
    vector_store_query_mode="hybrid", 
    similarity_top_k=2
    )

#Responding to a query
response = query_engine.query("三平方の定理とは？")
print(response, end="\n\n")


#Getting a part of Reference
"""print("Nodes:")
print(response.source_nodes[0].node.text, end="\n\n")
print(response.source_nodes[1].node.text, end="\n\n")"""


#Getting the title of the Reference
dict = {}
Dict = {}
Path = {}
key = []
for files in folder_list:
    path_list = glob.glob(files + "/*")
    for path in path_list:
        for i in range(2):
            with open(path, "r") as f:
                text = f.read()
                #Comparing the text of the node with the text of the response
                if re.search(response.source_nodes[i].node.text, text):
                    #pathとしてkeyを取得、textとしてvalueを取得
                    dict[path] = text
                    #pathの出力
                    """print(f"Pathの出力:\n{path}")"""
                    #keyのlist化
                    key.append(path)
                    
                    """print(type(re.sub(r'\..*\/', '', dict[path].keys())))"""

"""print(f"Pathのlistを出力:\n{key}", end = "\n\n\n")"""

with open("test.json") as f:
    d = json.load(f)
    """print(type(d), end="\n\n")"""
    for i in d.values():
        for j in key:
            #keyの中からファイル名だけを取得する。type=str.
            if i == re.sub(r'\..*\/', '', j).rstrip(".txt"):
                print(i)
                keys = [k for k, v in d.items() if v == i]
                #listを出力
                print(keys, end="\n\n")
                """print(type(keys), end="\n\n")"""
                """print(d.keys(i), end="\n\n")"""
                """print(dict[j], end="\n\n")
                Dict[i] = dict[j]
                Path[i] = j"""

"""for i in key:
    #keyの中からファイル名だけを取得する。type=str.
    print((re.sub(r'\..*\/', '', j)).rstrip(".txt"), end="\n\n")"""
"""print(dict.keys())"""

