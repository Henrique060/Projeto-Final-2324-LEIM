from haystack.document_stores import InMemoryDocumentStore
from haystack import Document
from haystack.document_stores import KeywordDocumentStore

class DocumentStoreModel(InMemoryDocumentStore):

    def __init__(self):
        self.model = super().__init__(use_bm25=True)

    def write_document(self, dataset):
        
        print("A escrever os documentos...")
        #self.model.write_documents([Document(content=dataset)])
        self.model.write_documents(dataset)