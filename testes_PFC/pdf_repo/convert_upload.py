from pdf_to_json_builder import PDFToJsonBuilder
from load_json import LoadJson
from upload_to_repo import UploadToRepo
from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi

class ConvertUpload:

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
        self.upload_repo = UploadToRepo(self.dataset, self.dataset_dict, self.hf_token,
                                        self.repo_id, self.api)

    def convert_upload(self, input_directory, output_directory):
        self.pdf_json_builder.convert_pdfs_in_directory(input_directory, output_directory)
        data = self.load_json.load_json_files_from_directory(output_directory)

        self.dataset = Dataset.from_list(data)
        self.dataset_dict = DatasetDict({"dataset": self.dataset})

        self.upload_repo.upload_to_repo()

    

if __name__ == "__main__":
    pdf_path = "pdf_repo"
    json_path = "json_repo"
    repo_id = "hmpm00/bul-id-bulas"
    api = HfApi()
    convert_upload = ConvertUpload(pdf_path, json_path, repo_id, api)


    
        