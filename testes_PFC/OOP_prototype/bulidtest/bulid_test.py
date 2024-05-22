

from OOP_prototype.openAI.doc_store.document_store import DocumentStoreModel
from OOP_prototype.openAI.rag_model.rag import RAG
#from OOP_prototype.openAI.retriever.bm_25_retriever import BM25RetrieverCustom
from OOP_prototype.openAI.bulid_man.bulid import BulID
from datasets import load_dataset
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever

#import logging



path = ""


## VERIFICAR QUE A ORDEM DO CODIGO É IMPORTANTE
## NESTE MOMENTO TEM DE SER CORRIGIDA A ORDEM E 
##   MUDAR O BULID PARA NAO RECEBER O RETRIEVER

#question = input("Coloque a sua questão ao modelo: ")

    
def filter_by_name(example, name):
    return example['name'] == name

"""
def logic_test_v1():
    # Inicia a lógica do processador das bulas
    #document_store = DocumentStoreModel()
    bul_id = BulID()
    bul_id.key_init()
    dataset = load_dataset("hmpm00/bul-id-bulas", split="train")
    document_med_name = dataset.filter(lambda example: filter_by_name(example, name))
    doc_store = InMemoryDocumentStore(use_bm25=True)
    bul_id.write_documents(dataset, doc_store, document_med_name)
    #key = "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"
    rag_model = RAG(doc_store)
    return rag_model
"""


def logic_load_dataset_bulid():
    bul_id = BulID()
    bul_id.key_init()
    dataset = load_dataset("hmpm00/bul-id-bulas", split="train")
    return dataset, bul_id

def logic_load_rag(dataset, bul_id, name):
    document_med_name = dataset.filter(lambda example: filter_by_name(example, name))
    doc_store = InMemoryDocumentStore(use_bm25=True)
    bul_id.write_documents(dataset, doc_store, document_med_name)
    #key = "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"
    rag_model = RAG(doc_store)
    return rag_model


"""
def logic_test_v1(med_name_to_fetch):
    
 
    bul_id = BulID()
    bul_id.key_init()

    doc_store = InMemoryDocumentStore(use_bm25=True)

    # Load dataset and filter by medication name
    dataset = load_dataset("hmpm00/bul-id-bulas", split="train")
    document_med_name = dataset.filter(lambda example: filter_by_name(example, med_name_to_fetch))

    # Write documents to the document store
    bul_id.write_documents(dataset, doc_store, document_med_name)

    # Initialize the RAG model
    rag_model = RAG(doc_store)

    return rag_model
    """

def ask_question(question, rag_model):
    rag_model.prompt_initializer(question)

#init()


## _________________________________________________ ESQUECER ISTO ABAIXO _______________________________________________

#answer = rag_model.model_answers(pipeline, question)
#print(answer)	

#model = logic_test_v1('nolotil')
#question = input("\n Apresente a sua questão ao modelo: ")
#ask_question(question, model)

#dataset, bul_id = logic_load_dataset_bulid()
#model = logic_load_rag(dataset, bul_id, 'nolotil')
#question = input("\n Apresente a sua questão ao modelo: ")
#ask_question(question, model)

