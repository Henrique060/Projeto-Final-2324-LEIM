from haystack.nodes import PromptNode, PromptTemplate, AnswerParser
from haystack.pipelines import Pipeline
from haystack.nodes import BM25Retriever

import logging

class RAG:

    def __init__(self, doc_store, model_name_or_path="gpt-3.5-turbo", key="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"):
        self.key = key
        self.doc_store = doc_store
        self.model_name_or_path = model_name_or_path

    def prompt_initializer(self, question):

        retriever = BM25Retriever(document_store=self.doc_store, top_k=2)
        print("A iniciar o RAG model...")
        rag_prompt= PromptTemplate(name="analysis-prompt",
                                   prompt_text="""Synthesize a comprehensive answer from the following text for the given question.
                             Provide a clear and concise response that summarizes the key points and information presented in the text.
                             Your answer should be in your own words and summarized to the maximum. If summarization
                             is not possible, the answer should be no longer than 200 words.
                             \n\n Related text: {join(documents)} \n\n Question: {query} \n\n Answer:""",
                    output_parser=AnswerParser(),)
        prompt_node = PromptNode(model_name_or_path="gpt-3.5-turbo", 
                                 api_key=self.key, 
                                 default_prompt_template=rag_prompt)

        pipeline = Pipeline()
        pipeline.add_node(component=retriever, name="retriever", inputs=["Query"])
        pipeline.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])
        
        print("RAG model iniciado com sucesso!")

        print("\n A iniciar a resposta do modelo...")
        answer = pipeline.run(query=question)
        print (answer["answers"][0].answer)
    
        #return pipeline
    
    """def pipeline_initializer(self):
        retriever = self.retriever
        prompt_node = self.promt_initializer()

        pipeline = Pipeline()
        pipeline.add_node(component=retriever, name="retriever", inputs=["Query"])
        pipeline.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])
        return pipeline
        """
    
    def model_answers(self, pipeline, question):
        print("\n A iniciar a resposta do modelo...")
        answer = pipeline.run(query=question)
        return (answer["answers"][0].answer)