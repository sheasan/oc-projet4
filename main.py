import datetime
from datetime import date
import string
import re
from enum import Enum
from typing import Union
import json

class Player:
    """test docstring"""
    class Gender(Enum):
        Homme = "Homme"
        Femme = "Femme"
    
    counter = 0

    ## Initialisation avec méthode spéciale __init__
    def __init__(self, nom, prenom, date_de_naissance, classement, gender, id = None):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.classement = classement
        self.gender = gender
        if id is None:
            self.id = Player.counter
            Player.counter += 1
        else:
            self.id = id

    ## Factorisation code vérification regex
    @staticmethod
    def _check_regex(value : str, nom : str = "nom"):
        if re.match("^[A-Za-z\- éèêëîïûüçâäôö]{2,20}$", value):
            return value
        else:
            raise AttributeError(f"Votre {nom} ne doit pas contenir de caractères spéciaux")

    ## Méthode get pour accèder aux attributs privés
    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom
    
    @property
    def date_de_naissance(self):
        return self.__date_de_naissance
    
    @property
    def classement(self):
        return self.__classement
    
    @property
    def gender(self):
        return self.__gender

    @property
    def id(self):
        return self.__id
    
    ## Méthode setter pour changer la valeur des attributs privés
    @nom.setter
    def nom(self, value : str):
        self.__nom = Player._check_regex(value)
    
    @prenom.setter
    def prenom(self, value : str):
        self.__prenom = Player._check_regex(value)
    
    @date_de_naissance.setter
    ## Utiliser Union (soit l'un ou l'autre)
    def date_de_naissance(self, value : str):
        ## Vérification format de date
        if isinstance(value, str) :
            try:
                dob = datetime.date.fromisoformat(value)
            except ValueError:
                raise ValueError("Format de date incorrect : veuillez renseigner sous cette forme AAAA-MM-JJ")
        
            today = date.today()
        
            age = today.year - dob.year

        ## Vérification de l'âge minimum requis
        if age < 12 :
            raise AttributeError("Vous devez avoir au moins 12 ans")
        else:
            self.__date_de_naissance = str(dob)
    
    @classement.setter
    def classement(self, value : int):
        if not isinstance(value, int):
            raise AttributeError("Veuillez entrer une donnée au format numéraire")
        elif value < 0 or value > 50:
            raise AttributeError("Veuillez entrer un nombre compris entre 0 et 50")
        else:
            self.__classement = value

    @gender.setter
    def gender(self, value: Union[str, Gender]):
        if isinstance(value, str):
            try:
                value = Player.Gender(value.title())
            except ValueError:
                raise AttributeError("Vous devez renseigner soit Homme, soit la valeur Femme")
        if isinstance(value, Player.Gender):
            self.__gender = str(value)
        else:
            raise AttributeError("...")
    
    @id.setter
    def id(self, value):
        if isinstance(value, int):
            print(Player.counter)
            if value == (Player.counter):
                print("Attention id doublons") 
            else:
                self.__id = value
        else:
            print("L'id doit être au format numérique")

    def __repr__(self):
       return "Nom: "+self.nom+" "+","+"Prénom: "+self.prenom+", "+"Date de naissance: "+str(self.date_de_naissance)+" ,"+"Classement: "+str(self.classement)+" ,"+"Sexe: "+str(self.gender)


try:
    player1 = Player("snow", "jon", "2000-06-18", 5, "Homme")
    player2 = Player("boris", "klein", "2000-06-18", 5, "Homme")
    ##player2 = Player("boris", "klein", "2000-06-18", 5, "Homme", 1)
    print(player1)
    ## Ajout code serialization
    serialization = json.dumps(player2.__dict__)
    with open( "datafile.json" , "w" ) as write:
        json.dump( serialization , write )
    print((serialization))
except AttributeError as nameError:
    print(nameError)

