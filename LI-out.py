from pathlib import Path
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor
from langchain.chat_models import ChatOpenAI
import os

from googletrans import Translator


os.environ["OPENAI_API_KEY"] = '<API_KEY>'

llm_predictor = LLMPredictor(
    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
)

loaded_index = GPTSimpleVectorIndex.load_from_disk('index.json')
query = input("質問を入力してください：")
response = loaded_index.query(query)
print(type(response))

"""tr = Translator()
result = tr.translate(response, dest='ja').text
print(result)"""
