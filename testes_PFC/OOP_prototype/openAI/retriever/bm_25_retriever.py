from getpass import getpass
import os
from haystack.nodes import BM25Retriever

class BM25RetrieverCustom:

    def __init__(self, top_k):
        self.top_k = top_k
        self._open_ai_key = "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"
    
    def key_init(self):
        #openai_key = os.getenv(self._open_ai_key, None) or getpass("Please enter your OpenAI API key: ")
        openai_key = "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"
        return openai_key
