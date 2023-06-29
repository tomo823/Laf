from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore
import pinecone
from llama_index import LLMPredictor, ServiceContext, GPTVectorStoreIndex
from llama_hub.confluence.base import ConfluenceReader
from langchain.chat_models import ChatOpenAI
import pinecone
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import PineconeVectorStore
from dotenv import load_dotenv
import gradio as gr
import os, sys
import graphsignal
import logging
from llama_hub.confluence.base import ConfluenceReader


OPENAI_API_KEY="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"
GRAPHSIGNAL_API_KEY=YOUR-GRAPHSIGNAL-API-KEY
CONFLUENCE_API_TOKEN=YOUR-CONFLUENCE-API-TOKEN
CONFLUENCE_USERNAME=YOUR-CONFLUENCE-USERNAME
PINECONE_API_KEY="b24cf74f-2854-4260-b087-7d32838b83f8"

load_dotenv()

# enable INFO level logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#configures Graphsignal tracer
graphsignal.configure(api_key=os.environ.get("GRAPHSIGNAL_API_KEY"), deployment='DevSecOpsKB')


base_url = "https://wenqiglantz.atlassian.net/wiki"
space_key = "SD"

loader = ConfluenceReader(base_url=base_url)
documents = loader.load_data(space_key=space_key, page_ids=[], include_attachments=True)


pinecone.init(api_key=os.environ["b24cf74f-2854-4260-b087-7d32838b83f8"], environment="us-west4-gcp-free")

# call pinecone to create index, dimension is for text-embedding-ada-002
pinecone.create_index("keyword-search", dimension=1536, metric="cosine", pod_type="Starter")
pinecone_index = pinecone.Index("confluence-wiki")

# build the PineconeVectorStore and GPTVectorStoreIndex
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context)