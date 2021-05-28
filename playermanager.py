import json
import main

class PlayerManager:
    def __init__(self):
        self.__registry = {}

    def load_from_json(self):
        ## deserialization
        with open('datafile.json') as json_file:
            data = json.load(json_file)

        ## Création boucle for pour parcourir la liste contenant different dictionnaires (corresspondant aux diff objet joueur)
        for dictionnary in data:
            player_object = main.Player(**dictionnary)
            ##print(player_object)
            self.__registry[player_object.id] = player_object

    def all(self):
        return list(self.__registry.values())

    def find_by_id(self, id):
        return self.__registry[id]

    def find(self, key):
        result = []
        for player in self.__registry.values():
            if key(player) :
                result.append(player)
        return result

if __name__ == "__main__":
    player_manager = PlayerManager()





