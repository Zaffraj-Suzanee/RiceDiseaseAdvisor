import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

VECTOR_PATH = os.path.join(
    BASE_DIR,
    "rag",
    "vectorstore"
)



def retrieve_documents(query, k=3):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(
        query,
        k=k
    )

    return docs


if __name__ == "__main__":

    question = "What are symptoms of rice blast disease?"

    results = retrieve_documents(question)

    for doc in results:
        print("\n--- DOCUMENT ---")
        print(doc.page_content[:500])