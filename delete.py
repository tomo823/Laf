import pinecone
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

import glob


pinecone.init(
    api_key="c53bdc0a-8999-428a-96e4-ada87a86cae9",
    environment="us-west4-gcp-free"
)


pinecone.delete_index('keyword-search')