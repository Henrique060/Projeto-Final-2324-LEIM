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

    def __init__(self, document_store, retriever, key = "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"):
        self.document_store = document_store
        self.retriever = retriever
        self.key = key

    def dataset_parsed(self, doc_path):
        print("A fazer parsing...")
        with open(doc_path) as f:
            parsed_data = json.load(f)
        print(parsed_data[0])
        return parsed_data[0]

    
    
