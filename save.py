import pinecone
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
import random
import itertools
import glob


pinecone.init(
    api_key="c53bdc0a-8999-428a-96e4-ada87a86cae9",
    environment="us-west4-gcp-free"
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
    "./movies/資料の活用"]

list = []

for files in folder_list:
    path_list = glob.glob(files + "/*")
    for path in path_list:
        with open(path, "r") as f:
            text = f.read()
            list.append(text)


model = SentenceTransformer('flax-sentence-embeddings/all_datasets_v3_mpnet-base')

all_embeddings = model.encode(list)


tokenizer = AutoTokenizer.from_pretrained('transfo-xl-wt103')

all_tokens = [tokenizer.tokenize(sentence.lower()) for sentence in list]


pinecone.list_indexes()

"""pinecone.create_index('keyword-search', dimension=1536, metric='cosine', shards=1, replicas=1)"""

index = pinecone.Index('keyword-search')


vector_dim = 1536
vector_count = 10000

def chunks(iterable, batch_size=100):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))



example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

# Upsert data with 100 vectors per upsert request
"""for ids_vectors_chunk in chunks(zip(all_embeddings, all_tokens), batch_size=100):
    index.upsert(vectors=ids_vectors_chunk)"""

print(all_embeddings)

"""for ids_vectors_chunk in chunks(example_data_generator, batch_size=100):
    index.upsert(vectors=ids_vectors_chunk)"""

"""upserts = []
for i, (embedding, tokens) in enumerate(zip(all_embeddings, all_tokens)):
    upserts.append((str(i), embedding.tolist(), {'tokens': tokens}))

index.upsert(vectors=upserts)"""