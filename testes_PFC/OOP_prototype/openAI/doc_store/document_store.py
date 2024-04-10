from haystack.document_stores import InMemoryDocumentStore
from haystack import Document

class DocumentStore:

    def __init__(self, store_model):
        store_model = InMemoryDocumentStore(use_bm25=True)
        self.store_model = store_model

    def write_documents(self, dataset):
        self.store_model.write_documents([Document(content=dataset)])
        return self.store_model