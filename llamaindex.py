from dotenv import load_dotenv
from pathlib import Path
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor
from langchain.chat_models import ChatOpenAI

import os
os.environ["OPENAI_API_KEY"] = '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'

load_dotenv()

SimpleCSVReader = download_loader("SimpleCSVReader")

llm_predictor = LLMPredictor(
    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
)

csv_path = Path('./article-urls.csv')

loader = SimpleCSVReader()
documents = loader.load_data(file=csv_path)

index = GPTSimpleVectorIndex.from_documents(documents)

query = 'allpeの特徴は？'
response = index.query(query)
print(response)

index.save_to_disk('index.json')
loaded_index = GPTSimpleVectorIndex.load_from_disk('index.json')