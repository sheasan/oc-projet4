import datetime
from datetime import date
import string
import re
from enum import Enum
from typing import Union

class Player:
    """test docstring"""
    class Gender(Enum):
        Homme = "Homme"
        Femme = "Femme"

    ## Initialisation avec méthode spéciale __init__
    def __init__(self, nom, prenom, date_de_naissance, classement, gender):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.classement = classement
        self.gender = gender
    
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
    
    ## Méthode setter pour changer la valeur des attributs privés
    @nom.setter
    def nom(self, nom : str):
        if re.match("^[A-Za-z\-éèêëîïûüçâäôö]{2,20}$", nom):
            self.__nom = nom
        else:
            raise AttributeError("Votre nom ne doit pas contenir de charactères spéciaux")
    
    @prenom.setter
    def prenom(self, prenom):
        if re.match("^[A-Za-z\-éèêëîïûüçâäôö]{2,20}$", prenom):
            self.__prenom = prenom
        else:
            raise AttributeError("Votre prenom ne doit pas contenir de charactères spéciaux")
    
    @date_de_naissance.setter
    def date_de_naissance(self, date_de_naissance):
        ## Vérification format de date
        try:
            dob = datetime.date.fromisoformat(date_de_naissance)
        except ValueError:
            raise AttributeError("Format de date incorrect : veuillez renseigner sous cette forme jj/mm/aaaa")
        
        today = date.today()
        
        age = today.year - dob.year

        ## Vérification de l'âge minimum requis
        if age < 12 :
            raise AttributeError("Vous devez avoir au moins 12 ans")
        else:
            self.__date_de_naissance = date_de_naissance
    
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
            self.__gender = value
        else:
            raise AttributeError("...")

    def __repr__(self):
       return "Nom: "+self.nom+" "+","+"Prénom: "+self.prenom+", "+"Date de naissance: "+str(self.date_de_naissance)+" ,"+"Classement: "+str(self.classement)+" ,"+"Sexe: "+str(self.gender)


try:
    player1 = Player("snow", "jon", "2000-06-18", 5, "Homme")
    print(player1)
except AttributeError as nameError:
    print(nameError)

