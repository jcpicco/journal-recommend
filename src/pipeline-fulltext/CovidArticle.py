# Clase CovidArticle
import json

class CovidArticle:
    def __init__(self, type, file_name):
        try:
            data = json.load(open("../data/document_parses/"+type+"_json/"+file_name ,"r"))

        except:
            raise ValueError("Tipo o documento no válido.")

        self.id = data["paper_id"]

        self.full_text = ""

        for d in data["body_text"]:
            self.full_text = self.full_text + " " + d["text"]
    