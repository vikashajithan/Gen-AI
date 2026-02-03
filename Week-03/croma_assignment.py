from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma

# Text data
text_embed = [
    "This is the best AI course",
    "AI is the future",
    "Hii this is vikash"
]

# Embedding model
embedding_new = HuggingFaceBgeEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Create Chroma vector store
vectorstore = Chroma.from_texts(
    texts=text_embed,
    embedding=embedding_new,
    persist_directory="My_croma_vectordb"
)

# Save to disk
vectorstore.persist()
