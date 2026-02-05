from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
 
text_embed = [
    "This is the best AI course",
    "AI is the future",
    "Hii this is vikash"
]

embedding_new = HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = FAISS.from_texts(text_embed,embedding_new)

vectorstore.save_local("My_first_vectordb")

retriever = vectorstore.as_retriever()

query = "AI?"

answer = retriever.invoke(query)


for docs in answer:
    print(docs.page_content)