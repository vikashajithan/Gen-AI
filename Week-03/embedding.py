from langchain_community.embeddings import HuggingFaceEmbeddings

hugging_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

texts = "This is a sample text for generating embeddings using HuggingFace model."

embeding = hugging_embeddings.embed_query(texts)

print(embeding[:5])

