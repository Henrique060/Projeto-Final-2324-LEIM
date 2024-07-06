import os
import json

class LoadJson:
    """ Classe responsável por carregar ficheiros JSON de uma diretoria. """
    def __init__(self, path_to_load):
        self.path_to_load = path_to_load

    def load_json_files_from_directory(self, path_to_load):
        """ Carrega os ficheiros JSON da diretoria onde se encontram. """
        data = [] # Aqui metem-se os dados, conteúdo dos ficheiros JSON
        for filename in os.listdir(path_to_load):
            if filename.endswith(".json"): # Verifica se o ficheiro é um JSON
                with open(os.path.join(path_to_load, filename), 'r', encoding='utf-8') as f: # Tem de ter encoding utf-8 ou então perdem-se acentos
                    json_data = json.load(f)
                    if isinstance(json_data.get("content"), list):
                        json_data["content"] = "\n".join(json_data["content"])  # Certifica-se que o conteúdo é uma string
                    data.append(json_data)
        return data