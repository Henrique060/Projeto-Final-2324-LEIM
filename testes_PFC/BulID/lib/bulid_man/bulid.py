from lib.rag_model.rag import RAG
from datasets import load_dataset
from haystack.document_stores import InMemoryDocumentStore
import logging

class BulID:
    """ Classe que permite a gestão da lógica do modelo RAG, 
        bem como o acesso à API do OpenAI.

        É a classe central ao programa completo, gerindo a lógica
        total do programa, concatenado as classes e funções que
        permitem a comunicação entre si e a execução correta do
        programa.

        Permite modularizar o programa de modo a que este seja utilizado
        como uma API, sem que haja necessidade de alterar o código central,
        utilizando seja em consola ou em interface gráfica.
    """
    def __init__(self):
        self.open_ai_key = "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"
        self.doc_store = None
        logging.basicConfig(format="%(levelname)s - %(name)s - %(message)s, level=logging.WARNING")
        logging.getLogger("haystack").setLevel(logging.INFO)
    
    def key_init(self):
        """ Retorna a chave de acesso à API do OpenAI, para uso do LLM. """
        return self.open_ai_key

    def write_documents(self, doc_store, med_name):
        """Permite escrever os documentos no doc_store, que é um
            InMemoryDocumentStore, para que possam ser utilizados
            pelo modelo RAG."""
        
        doc_store.write_documents(med_name)

    def filter_by_name(self, example, name):
        """ Permite que seja filtrado o dataset de acordo com
            o nome do medicamento que se pretende buscar.
        """
        return example['name'] == name
    
    def logic_load_dataset_bulid(self):
        # Inicia e retorna o dataset e a instância do modelo.
        #    Faz uso da chave da API para acesso ao LLM.
        
        self.key_init()
        dataset = load_dataset("hmpm00/bul-id-bulas-final", split="dataset")
        return dataset, self
    
    def logic_load_rag(self, name):
        """ Incia a lógica do modelo RAG.
        
            Relativa, na framework, à parte de Augmented Generation, 
            alimenta ao LLM o contexto e questão para que se possa 
            gerar uma resposta mais completa e contextualizada.
        """
        self.doc_store = InMemoryDocumentStore(use_bm25=True)
        dataset = load_dataset("hmpm00/bul-id-bulas-final", split="dataset")
        document_med_name = dataset.filter(lambda example: self.filter_by_name(example, name))
        self.write_documents(self.doc_store, document_med_name)
        print("Num de documentos: ", self.doc_store.get_document_count())
        rag_model = RAG(self.doc_store)
        return rag_model
    
    def ask_question(self, question, rag_model):
        """ Permite realizar a questão ao modelo RAG, sem interrupções
            do programa ou da lógica do modelo em si.
        """
        return rag_model.prompt_initializer(question)

    
    
