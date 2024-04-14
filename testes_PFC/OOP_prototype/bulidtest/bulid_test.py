from testes_PFC.OOP_prototype.openAI.doc_store.document_store import DocumentStoreModel
from testes_PFC.OOP_prototype.openAI.rag_model.rag import RAG
from testes_PFC.OOP_prototype.openAI.retriever.bm_25_retriever import BM25RetrieverCustom
from testes_PFC.OOP_prototype.openAI.bulid_man.bulid import BulID

import logging


logging.basicConfig(format="%(levelname)s - %(name)s - %(message)s, level=logging.WARNING")
logging.getLogger("haystack").setLevel(logging.INFO)

path = "testes_PFC/OOP_prototype/benuron.json"


## VERIFICAR QUE A ORDEM DO CODIGO É IMPORTANTE
## NESTE MOMENTO TEM DE SER CORRIGIDA A ORDEM E 
##   MUDAR O BULID PARA NAO RECEBER O RETRIEVER

#question = input("Coloque a sua questão ao modelo: ")

    
def logic_test_v1(quest):
    """ Inicia a lógica do processador das bulas """
    document_store = DocumentStoreModel()
    bul_id = BulID()
    bul_id.key_init()
    dataset = bul_id.dataset_parsed(path)
    doc_store = bul_id.init_doc_store()
    bul_id.write_documents(dataset, doc_store)
    #key = "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"
    rag_model = RAG(doc_store)
    pipeline = rag_model.prompt_initializer(quest)

#init()


## _________________________________________________ ESQUECER ISTO ABAIXO _______________________________________________

#answer = rag_model.model_answers(pipeline, question)
#print(answer)	


question = "Benuron pode ser tomado por quem tem intolerância à lactose?"
logic_test_v1(question)