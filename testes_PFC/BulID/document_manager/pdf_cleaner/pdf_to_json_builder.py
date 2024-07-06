import PyPDF2
import os
import json
import re
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

class PDFToJsonBuilder:
    """ Classe responsável por converter ficheiros PDF para JSON.
        Efetua a limpeza via stemming e expressões regulares, reduzindo tamanhos de tokens.
    """
    def __init__(self, pdf_path, json_path):
        self.pdf_path = pdf_path
        self.json_path =json_path

    def clean_and_stem_text(self, text):
        """ Limpa o texto e aplica stemming ao mesmo. """
        stemmer = SnowballStemmer(language='portuguese')

        text = text.lower()
        text = re.sub(r'([^\w\s])\1+', r'\1', text)
        text = re.sub(r'[^\w\s,]', '', text)
        text = re.sub(r'\b(?!\d+)\w{1,2}\b', '', text)
        text = re.sub(r'\s+', ' ', text).strip()

        words = word_tokenize(text)

        stemmed_words = [stemmer.stem(word) for word in words]
        cleaned_text = ' '.join(stemmed_words)

        return cleaned_text

    def pdf_to_json(self, pdf_path):
        """ Converte um ficheiro PDF para JSON. Aplica a limpeza e stemming. """
        with open(pdf_path, 'rb') as pdf_file:
            read_pdf = PyPDF2.PdfReader(pdf_file)
            number_of_pages = len(read_pdf.pages)
            pdf_text = []

            for i in range(number_of_pages):
                page = read_pdf.pages[i]
                extracted_text = page.extract_text()
                if extracted_text:
                    cleaned_text = self.clean_and_stem_text(extracted_text)
                    pdf_text.append(cleaned_text)

            pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
            pdf_data = {"name": pdf_name, "content": " ".join(pdf_text)}

        return pdf_data


    def convert_pdfs_in_directory(self, input_directory, output_directory):
        """ Converte todos os ficheiros PDF de uma diretoria para JSON. """
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for filename in os.listdir(input_directory):
            if filename.endswith(".pdf"):
                input_path = os.path.join(input_directory, filename)
                pdf_data = self.pdf_to_json(input_path)

                output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.json")
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(pdf_data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    pdf_path = "BulID/document_manager/repo_bulas_pdf"
    json_path = "BulID/document_manager/repo_bulas_json"
    pdf_json_builder = PDFToJsonBuilder(pdf_path, json_path)
    pdf_json_builder.convert_pdfs_in_directory(pdf_path, json_path)
