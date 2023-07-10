
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor
from langchain.chat_models import ChatOpenAI
import os


os.environ["OPENAI_API_KEY"] = '<API_KEY>'

llm_predictor = LLMPredictor(
    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
)

files = []

SimpleCSVReader = download_loader("SimpleCSVReader")
loader = SimpleCSVReader()

documents = loader.load_data("./movies/【高校数学1】数と式/【高校数学1  数と式】1次不等式：絶対値を含む方程式・不等式をわかりやすく解説！ [mjXmorzYsLQ].txt")

index = GPTSimpleVectorIndex.from_documents(documents)

query = '一次方程式の解き方は？'
response = index.query(query)
print(response)

index.save_to_disk('index.json')
loaded_index = GPTSimpleVectorIndex.load_from_disk('index.json')


