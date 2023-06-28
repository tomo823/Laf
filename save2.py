import os
import logging
import sys
import pinecone
import glob
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai
import llama_index


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


os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = "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"


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)


api_key = "c53bdc0a-8999-428a-96e4-ada87a86cae9"
pinecone.init(api_key=api_key, environment="us-west4-gcp-free", pod_type="starter")
"""pinecone.create_index('keyword-search', dimension=1536, metric="dotproduct", shards=1, replicas=1, pod_type="starter")"""

pinecone.describe_index("keyword-search")

pinecone_index = pinecone.Index('keyword-search')


#vector store作成用
"""vector_store = PineconeVectorStore(
    pinecone_index=pinecone_index,
    add_sparse_vector=True,
)"""
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


#documentsをindexにupsertしている
"""index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)"""
#pineconeからindexを取得
index = VectorStoreIndex.from_vector_store(vector_store)


query_engine = index.as_query_engine(
    vector_store_query_mode="hybrid", 
    similarity_top_k=2
    )

response = query_engine.query("三平方の定理とは？")
print(llama_index.indices.response.base_builder)
print(llama_index.indices.utils)
