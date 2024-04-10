import getpass
import os


class BM25Retriever:

    def __init__(self, document_store, top_k):
        self.document_store = document_store
        self.top_k = top_k
        self.openai_key = "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"

    def retrieve(self, retriever):
        return retriever(self.document_store, self.top_k)
    
    def key_init(self):
        openai_key = os.getenv(self.openai_key, None) or \
            getpass("Please enter your OpenAI API key: ")
        return openai_key