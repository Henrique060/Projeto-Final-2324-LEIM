from haystack.nodes import PromptNode, PromptTemplate, AnswerParser
from haystack.pipelines import Pipeline
from haystack.nodes import BM25Retriever
import logging



class RAG:
    """ Classe responsável pela lógica da framework RAG.

        RAG - Retrieval Augmented Generation. Framework que permite
        gerar respostas através de perguntas feitas a LLMs cujo conhecimento
        foi expandido por um modelo de recuperação de informação. 

        Divide-se em três fases:
        - Retrieval: Utiliza um retriever, para que, através de 'semantic search',
        seja possível obter contexto e informação relevante para a questão
        - Augmented: Através da alimentação do contexto e da questão ao LLM,
        é possível gerar uma resposta contextualizada
        - Generation: A resposta gerada é apresentada ao utilizador, de forma 
        concisa, clara e gramaticalmente correta
    """

    def __init__(self, doc_store, model_name_or_path="gpt-3.5-turbo", key="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"):
        self.key = key
        self.doc_store = doc_store
        self.model_name_or_path = model_name_or_path

        logging.basicConfig(format="%(levelname)s - %(name)s - %(message)s, level=logging.WARNING")
        logging.getLogger("haystack").setLevel(logging.INFO)

    def prompt_initializer(self, question):
        """ Função responsável pela questão colocada ao modelo RAG.
         
            Inicial o retriever, que tem o papel de 'motor de busca' da informação,
            relativamente ao passo de 'Retrieval' da framework RAG.
            
            Utiliza o BM25Retriever, que atribui aos documentos uma pontuação
            de 'relevância', tendo em quanto a frequência das palavras-chave
            contextualizadas à questão colocada ao modelo. Esta frequência
            apresenta um peso que será maior quanta maior a sua correlação.
            
            Após a obtenção do contexto, via Retrieval, e alimentado ao modelo
            a informação, no passo Augmented, para que se possa gerar uma resposta
            contextualizada, no passo Generation.
            
            É importante que possa ser alimentado com documentos diferentes,
            sendo que a função está modularizada para que não haja qualquer
            interrupção do modelo.
        """
        retriever = BM25Retriever(document_store=self.doc_store, top_k=2)
        print("A iniciar o RAG model...")
        rag_prompt= PromptTemplate(name="analysis-prompt",
                                   prompt_text="""Synthesize a comprehensive answer from the following text for the given question.
                                        Provide a clear and concise response that summarizes the key points and information presented in the text.
                                        Your answer should be in your own words and summarized to 50 words.
                                        Always answer in Portuguese.
                                        \n\n Related text: {join(documents)} \n\n Question: {query} \n\n Answer:""",
                    output_parser=AnswerParser())
        prompt_node = PromptNode(model_name_or_path=self.model_name_or_path, 
                                 api_key=self.key, 
                                 default_prompt_template=rag_prompt)

        pipeline = Pipeline()
        pipeline.add_node(component=retriever, name="retriever", inputs=["Query"])
        pipeline.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])
        
        print("RAG model iniciado com sucesso!")
        print("\n A iniciar a resposta do modelo...")

        answer = pipeline.run(query=question)
        print(answer["answers"][0].answer)
    
        return (answer["answers"][0].answer)
    