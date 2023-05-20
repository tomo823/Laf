from pathlib import Path
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor
from langchain.chat_models import ChatOpenAI
import os

from googletrans import Translator

from typing import List
from llama_index.data_structs.node_v2 import DocumentRelationship
from llama_index.response.schema import RESPONSE_TYPE
from llama_index import Document


os.environ["OPENAI_API_KEY"] = '<API_KEY>'

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

def print_source_of_response(response: RESPONSE_TYPE, documents: List[Document]):
    for node in response.source_nodes:
        if DocumentRelationship.SOURCE not in node.node.relationships:
            print("no source doc found")
            continue
        source_doc_id = node.node.relationships[DocumentRelationship.SOURCE]
        source_docs = [doc for doc in documents if doc.doc_id == source_doc_id]
        if len(source_docs) == 0:
            print("no source doc found")
            continue
        elif len(source_docs) == 1:
            source_doc = source_docs[0]
            print(source_doc.get_text())
        else:
            print("More than one source doc found")
            continue

loaded_index = GPTSimpleVectorIndex.load_from_disk('index.json')
query = input("質問を入力してください：")
response = loaded_index.query(query)
print(response)

print_source_of_response(response, folder_list)

"""tr = Translator()
result = tr.translate(response, dest='ja').text
print(result)"""
