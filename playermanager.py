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
    player_manager.load_from_json()
    print(player_manager.all())
    print(player_manager.find_by_id(2))
    print(player_manager.find(lambda x: x.gender == main.Player.Gender.Homme))

## chargement du fichier json
"""with open('datafile.json') as json_file:
    data = json.load(json_file)

## dictionnaire vide
registry = {}

## parcourir la liste de donnée et sérialisation en objet de class avec ajout dans le dictionnaire
for dictionnary in data:
    player_object = main.Player(**dictionnary)
    registry[player_object.id] = player_object
print(registry)"""

## Le resultat n'est pas bon car le gender du setter est converti en str (ligne 115) à corriger





