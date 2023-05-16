
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor,SimpleDirectoryReader
from langchain.chat_models import ChatOpenAI
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor
import os


os.environ["OPENAI_API_KEY"] = '<API_KEY>'

llm_predictor = LLMPredictor(
    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
)


SimpleCSVReader = download_loader("SimpleCSVReader")
loader = SimpleCSVReader()


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
    index = GPTSimpleVectorIndex.from_documents(documents=documents)
    index.save_to_disk('index.json')


index.save_to_disk('index.json')