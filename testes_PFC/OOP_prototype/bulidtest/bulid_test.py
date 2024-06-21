from OOP_prototype.openAI.rag_model.rag import RAG
from OOP_prototype.openAI.bulid_man.bulid import BulID
from datasets import load_dataset
from haystack.document_stores import InMemoryDocumentStore


    
def filter_by_name(example, name):
    return example['name'] == name


def logic_load_dataset_bulid():
    bul_id = BulID()
    bul_id.key_init()
    dataset = load_dataset("hmpm00/bul-id-bulas", split="train")
    return dataset, bul_id

def logic_load_rag(dataset, bul_id, name):
    document_med_name = dataset.filter(lambda example: filter_by_name(example, name))
    doc_store = InMemoryDocumentStore(use_bm25=True)
    bul_id.write_documents(doc_store, document_med_name)
    rag_model = RAG(doc_store)
    return rag_model


def ask_question(question, rag_model):
    return rag_model.prompt_initializer(question)
    

## Testar

#dataset, bul_id = logic_load_dataset_bulid()
#model = logic_load_rag(dataset, bul_id, 'nolotil')
#question = input("\n Apresente a sua questão ao modelo: ")
#ask_question(question, model)


