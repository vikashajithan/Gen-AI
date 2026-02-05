import os
os.environ["GROQ_API_KEY"] ="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"


import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# ------------------------
# Load LLM (Groq)
# ------------------------
llm = ChatGroq(model="llama-3.1-8b-instant")

# ------------------------
# Load Embeddings
# ------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ------------------------
# Knowledge Base
# ------------------------
texts = [
    "RAG means Retrieval Augmented Generation.",
    "Self-RAG allows the model to check and improve its own answers.",
    "FAISS is a vector database for similarity search."
]

docs = [Document(page_content=t) for t in texts]

db = FAISS.from_documents(docs, embeddings)

# ------------------------
# Functions
# ------------------------
def retrieve(query):
    results = db.similarity_search(query, k=2)
    return "\n".join([r.page_content for r in results])

def generate(question, context):
    prompt = f"""
Context:
{context}

Question: {question}
Answer:
"""
    return llm.invoke(prompt).content

def self_check(question, answer):
    prompt = f"""
Is this answer correct and helpful?

Question: {question}
Answer: {answer}

Reply YES or NO only.
"""
    return llm.invoke(prompt).content

def improve(question, context, answer):
    prompt = f"""
Improve the answer using context.

Context:
{context}
Old Answer: {answer}
Better Answer:
"""
    return llm.invoke(prompt).content

def self_rag(question):
    context = retrieve(question)
    answer = generate(question, context)
    check = self_check(question, answer)

    if "NO" in check:
        answer = improve(question, context, answer)

    return answer

# ------------------------
# STREAMLIT UI
# ------------------------

st.title("🤖 Self-RAG Question Answering App")

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question:
        answer = self_rag(question)
        st.success("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
