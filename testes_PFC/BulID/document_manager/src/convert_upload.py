from document_manager.pdf_cleaner.pdf_to_json_builder import PDFToJsonBuilder
from document_manager.uploader.load_json import LoadJson
from document_manager.uploader.upload_to_repo import UploadToRepo
from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi

class ConvertUpload:
    """ Classe responsável por converter ficheiros PDF para JSON
        fazendo upload para um repositório à escolha.

        Reúne toda a lógica para funcionamento via command line.
    """

    def __init__(self, pdf_path, json_path, repo_id, api):
        self.pdf_path = pdf_path
        self.json_path = json_path
        self.dataset = None
        self.dataset_dict = None
        self.hf_token = "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"
        self.repo_id = repo_id
        self.api = api

        self.pdf_json_builder = PDFToJsonBuilder(self.pdf_path, self.json_path)
        self.load_json = LoadJson(self.json_path)
        

    def convert_upload(self, input_directory, output_directory):
        """ Converte ficheiros PDF para JSON e faz upload para um repositório. """
        print("A converter de PDF para JSON...")
        self.pdf_json_builder.convert_pdfs_in_directory(input_directory, output_directory)
        print("A carregar os ficheiros JSON...")
        data = self.load_json.load_json_files_from_directory(output_directory)

        print("A criar o dataset...")
        self.dataset = Dataset.from_list(data)
        self.dataset_dict = DatasetDict({"dataset": self.dataset})

        self.upload_repo = UploadToRepo(self.dataset, self.dataset_dict, self.hf_token,
                                        self.repo_id, self.api)
        
        print("A fazer upload dos ficheiros para o repositório...")
        self.upload_repo.upload_to_repo()
        print("Upload concluído com sucesso!")

    

if __name__ == "__main__":
    pdf_path = "BulID/document_manager/repo_bulas_pdf"
    json_path = "BulID/document_manager/repo_bulas_json"
    repo_id = "hmpm00/bul-id-bulas-final"
    api = HfApi()
    convert_upload = ConvertUpload(pdf_path, json_path, repo_id, api)
    convert_upload.convert_upload(pdf_path, json_path)


    
        