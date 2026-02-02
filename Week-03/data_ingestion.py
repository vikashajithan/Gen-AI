"""
from langchain_community.document_loaders import TextLoader

test = TextLoader("demo.txt")

test.load()
"""
"""
from langchain_community.document_loaders import PyPDFLoader

test2 = PyPDFLoader("LLM.pdf")

test2.load()
"""
"""
from langchain_community.document_loaders import WebBaseLoader

test3 = WebBaseLoader(web_path="https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/")

test3.load()
"""

"""
from langchain_community.document_loaders import ArxivLoader

test4 = ArxivLoader(query="1706.03762")

test4.load()
"""

from langchain_community.document_loaders import WikipediaLoader

test5 = WikipediaLoader(query="AI agents",load_max_docs=2)

test5.load()

print(test5.load())