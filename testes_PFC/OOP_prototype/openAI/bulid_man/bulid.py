from haystack.document_stores import InMemoryDocumentStore
from haystack import Document
from datasets import load_dataset
from haystack.nodes import BM25Retriever

import os
from getpass import getpass
from haystack.nodes import PromptNode, PromptTemplate, AnswerParser
from haystack.pipelines import Pipeline
import logging
import pandas as pd
import json

class BulID:

    def __init__(self):
        self._open_ai_key = "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"

    def dataset_parsed(self, doc_path):
        print("A fazer parsing...")
        with open(doc_path) as f:
            parsed_data = json.load(f)
        print(parsed_data[0])
        return parsed_data[0]
    
    def key_init(self):
        #openai_key = os.getenv(self._open_ai_key, None) or getpass("Please enter your OpenAI API key: ")
        openai_key = "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"
        return openai_key
    
    def init_doc_store(self):
        return InMemoryDocumentStore(use_bm25=True)

    def write_documents(self, dataset, doc_store, med_name):

        print("A escrever os documentos...")
        doc_store.write_documents(med_name)

    
    
