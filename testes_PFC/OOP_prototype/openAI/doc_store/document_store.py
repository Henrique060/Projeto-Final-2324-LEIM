from haystack.document_stores import InMemoryDocumentStore
from haystack import Document
from haystack.document_stores import KeywordDocumentStore

class DocumentStoreModel() :

    def __init__(self):
        self.store_model = InMemoryDocumentStore(use_bm25=True)

    def write_documents(self, dataset):
        print("A escrever os documentos...")
        self.store_model.write_documents([Document(content=dataset)])