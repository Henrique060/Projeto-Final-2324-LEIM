from datasets import Dataset, DatasetDict
from huggingface_hub import create_repo

class UploadToRepo:
    """ Classe que realiza o upload de um dataset para um repositório,
        nomeadamente o Hugging Face Hub.
    """
    def __init__(self, dataset, dataset_dict, hf_token,
                 repo_id, api):
        self.dataset = dataset
        self.dataset_dict = dataset_dict
        self.hf_token = hf_token
        self.repo_id = repo_id
        self.api = api

    def call_api(self):
        return self.api

    def upload_to_repo(self):
        """ Cria o repositório em questão e adiciona os dados
            ao mesmo.
        """
        
        if self.api != None:
            self.call_api()
        create_repo(self.repo_id, token=self.hf_token,
                    private=False, exist_ok=True)
        self.dataset_dict.push_to_hub(repo_id=self.repo_id,
                                      token=self.hf_token)
        