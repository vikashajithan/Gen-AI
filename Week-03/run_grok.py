"""Run Grok (langchain_xai) embeddings only.

This script attempts to import `langchain_xai` and run a single embedding.
If the import fails it will exit with a non-zero status and print the error.
"""

import sys

try:
    from langchain_xai.embeddings import XAIEmbeddings
except Exception as e:
    print("ERROR: could not import langchain_xai:", e, file=sys.stderr)
    sys.exit(2)

try:
    emb = XAIEmbeddings(model="grok-embedding")
    vec = emb.embed_query("Hello Grok")
    # Print first five values for quick verification
    print(vec[:5])
except Exception as e:
    print("ERROR: failed to get embeddings:", e, file=sys.stderr)
    sys.exit(3)
