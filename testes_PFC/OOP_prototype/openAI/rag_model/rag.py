from haystack.nodes import PromptNode, PromptTemplate, AnswerParser
from haystack.pipelines import Pipeline

class RAG:

    def __init__(self, key, retriever, prompt_node, model_name_or_path="gpt-3.5-turbo"):
        self.key = key
        self.retriever = retriever
        self.prompt_node = prompt_node
        self.model_name_or_path = model_name_or_path

    def promt_initializer(self, key):
        rag_prompt= PromptTemplate(name="analysis-prompt",
                                   prompt_text="""Synthesize a comprehensive answer from the following text for the given question.
                             Provide a clear and concise response that summarizes the key points and information presented in the text.
                             Your answer should be in your own words and summarized to the maximum. If summarization
                             is not possible, the answer should be no longer than 200 words.
                             \n\n Related text: {join(documents)} \n\n Question: {query} \n\n Answer:""",
                    output_parser=AnswerParser(),)
        prompt_node = PromptNode(model_name_or_path=self.model_name_or_path, 
                                 api_key=key, 
                                 default_prompt_template=rag_prompt)
        return prompt_node
    
    def pipeline_initializer(self):
        retriever = self.retriever
        prompt_node = self.promt_initializer(self.key)

        pipeline = Pipeline()
        pipeline.add_node(component=retriever, name="retiever", inputs=["Query"])
        pipeline.add_node(component=prompt_node, name="prompt", inputs=["retiever"])
        return pipeline
    
    def model_answers(self, pipeline, question):
        pipeline = self.pipeline_initializer()
        answer = pipeline.run(query=question)
        return answer["answers"][0].answer