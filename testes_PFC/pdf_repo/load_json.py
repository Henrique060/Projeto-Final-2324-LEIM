import os
import json

class LoadJson:
    def __init__(self, path_to_load):
        self.path_to_load = path_to_load

    def load_json_files_from_directory(self):
        data = []
        for filename in os.listdir(self.path_to_load):
            if filename.endswith(".json"):
                with open(os.path.join(self.path_to_load, filename), 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                    if isinstance(json_data.get("content"), list):
                        json_data["content"] = "\n".join(json_data["content"])  # Ensure content is a single string
                    data.append(json_data)
        return data