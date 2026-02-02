from langchain_community.document_loaders import PyPDFLoader

textsplitter = PyPDFLoader("LLM.pdf")

spliter = textsplitter.load()

full_text = "\n".join([doc.page_content for doc in spliter])



from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts2 = text_splitter.split_text(full_text)
print(texts2)


