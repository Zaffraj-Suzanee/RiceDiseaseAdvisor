from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load documents

loader = PyPDFDirectoryLoader(
    "data/pdfs"
)

documents = loader.load()


print("Documents:", len(documents))


# Chunking

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


chunks = splitter.split_documents(documents)


print("Chunks:", len(chunks))


# Embeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Create vector database

vectorstore = FAISS.from_documents(
    chunks,
    embedding_model
)


vectorstore.save_local(
    "rag/vectorstore"
)


print("Vector database created!")