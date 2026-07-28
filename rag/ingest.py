import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


PDF_PATH = os.path.join(
    BASE_DIR,
    "data",
    "pdfs"
)


VECTOR_PATH = os.path.join(
    BASE_DIR,
    "rag",
    "vectorstore"
)


loader = PyPDFDirectoryLoader(PDF_PATH)

documents = loader.load()

print("Documents:", len(documents))


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


chunks = splitter.split_documents(documents)

print("Chunks:", len(chunks))


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.from_documents(
    chunks,
    embedding_model
)


vectorstore.save_local(VECTOR_PATH)


print("Vector database created!")