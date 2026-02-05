import os
os.environ["GROQ_API_KEY"] ="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"


import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# ------------------------
# Load LLM
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
    "Self-RAG allows a model to evaluate and improve its own answers.",
    "Corrective RAG fixes mistakes using retrieved context.",
    "Fusion RAG combines results from multiple searches.",
    "FAISS is a vector database for similarity search."
]

docs = [Document(page_content=t) for t in texts]
db = FAISS.from_documents(docs, embeddings)

# ------------------------
# BASIC RETRIEVE
# ------------------------
def retrieve(query):
    results = db.similarity_search(query, k=3)
    return "\n".join([r.page_content for r in results])

# ------------------------
# GENERATE
# ------------------------
def generate(question, context):
    prompt = f"""
Context:
{context}

Question: {question}
Answer:
"""
    return llm.invoke(prompt).content

# ======================================================
# ✅ SELF RAG
# ======================================================

def self_check(question, answer):
    prompt = f"""
Is this answer correct?

Question: {question}
Answer: {answer}

Reply YES or NO.
"""
    return llm.invoke(prompt).content

def self_rag(question):
    context = retrieve(question)
    answer = generate(question, context)
    verdict = self_check(question, answer)

    if "NO" in verdict:
        answer = generate(question, context)

    return answer

# ======================================================
# ✅ CORRECTIVE RAG
# ======================================================

def corrective_rag(question):
    context = retrieve(question)

    prompt = f"""
Use the context to correct any mistakes.

Context:
{context}

Question: {question}
Final Correct Answer:
"""
    return llm.invoke(prompt).content

# ======================================================
# ✅ FUSION RAG
# ======================================================

def fusion_rag(question):
    queries = [
        question,
        f"Explain {question}",
        f"Definition of {question}"
    ]

    all_docs = []
    for q in queries:
        all_docs.extend(db.similarity_search(q, k=2))

    fused_context = "\n".join(
        list(set([doc.page_content for doc in all_docs]))
    )

    return generate(question, fused_context)

# ------------------------
# STREAMLIT UI
# ------------------------

st.title("🤖 Advanced RAG App")

mode = st.selectbox(
    "Choose RAG Mode",
    ["Self-RAG", "Corrective-RAG", "Fusion-RAG"]
)

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question:
        if mode == "Self-RAG":
            answer = self_rag(question)
        elif mode == "Corrective-RAG":
            answer = corrective_rag(question)
        else:
            answer = fusion_rag(question)

        st.success("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
