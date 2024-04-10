from openAI.doc_store.document_store import DocumentStoreModel
from openAI.rag_model.rag import RAG
from openAI.retriever.bm_25_retriever import BM25Retriever
from openAI.bulid_man.bulid import BulID

from haystack.document_stores import InMemoryDocumentStore
from datasets import load_dataset
from haystack.nodes import BM25Retriever
import os
from getpass import getpass
from haystack.nodes import PromptNode, PromptTemplate, AnswerParser
from haystack.pipelines import Pipeline
import logging
import pandas as pd
import json
import logging


logging.basicConfig(format="%(levelname)s - %(name)s - %(message)s, level=logging.WARNING")
logging.getLogger("haystack").setLevel(logging.INFO)


## VERIFICAR QUE A ORDEM DO CODIGO É IMPORTANTE
## NESTE MOMENTO TEM DE SER CORRIGIDA A ORDEM E 
##   MUDAR O BULID PARA NAO RECEBER O RETRIEVER
document_store = DocumentStoreModel()
bul_id = BulID(document_store, bm_25_retriever)
dataset = bul_id.dataset_parsed(path)
document_store.write_documents(dataset)
bm_25_retriever = BM25Retriever(document_store, 2)
key = "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"
rag_model = RAG(bm_25_retriever)


path = "testes_PFC/OOP_prototype/benuron.json"



pipeline = rag_model.pipeline_initializer()
question = "Qual o princípio ativo do benuron?"
answer = rag_model.model_answers(pipeline, question)
print(answer)	




