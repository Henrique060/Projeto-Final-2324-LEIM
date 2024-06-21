import PyPDF2
import os
import json

class PDFToJsonBuilder:

    def __init__(self, pdf_path, json_path):
        self.pdf_path = pdf_path
        self.json_path =json_path

    def pdf_to_json(self, pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            read_pdf = PyPDF2.PdfReader(pdf_file)
            number_of_pages = len(read_pdf.pages)
            pdf_text = []

            for i in range(number_of_pages):
                page = read_pdf.pages[i]
                pdf_text.append(page.extract_text())
        
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        pdf_data = {"name": pdf_name, "content":"\n".join(pdf_text)}

        return pdf_data


    def convert_pdfs_in_directory(self, input_directory, output_directory):
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for filename in os.listdir(input_directory):
            if filename.endswith(".pdf"):
                input_path = os.path.join(input_directory, filename)
                pdf_data = self.pdf_to_json(input_path)

                output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.json")
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(pdf_data, f, ensure_ascii=False, indent=4)
