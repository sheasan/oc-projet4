import json
import main

class PlayerManager:
    def __init__(self):
        self.registry = {}

    def load_from_json(self):
        ## deserialization
        with open('datafile.json') as json_file:
            data = json.load(json_file)
            print(type(data))
    
        ## Création boucle for pour parcourir la liste contenant different dictionnaires (corresspondant aux diff objet joueur)



