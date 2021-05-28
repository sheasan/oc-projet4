from enum import Enum
import re
import datetime
from datetime import date
from typing import Union
import playermanager
import main

class Tournament:

    class TimeControlRule(Enum):
        Blitz = "Blitz"
        Bullet = "Bullet"
        FastMove = "FastMove"

    ## Initialisation avec méthode spéciale __init__
    def __init__(self, nom, lieu, date, tournees, players, ctrl_temps, description, nbr_tour = 4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_tour = nbr_tour
        self.tournees = tournees
        self.players = players
        self.ctrl_temps = ctrl_temps
        self.description = description
        

    ## Méthode get pour accèder aux attributs privés
    @property
    def nom(self):
        return self.__nom

    @property
    def lieu(self):
        return self.__lieu
    
    @property
    def date(self):
        return self.__date
    
    @property
    def nbr_tour(self):
        return self.__nbr_tour
    
    @property
    def ctrl_temps(self):
        return self.__ctrl_temps

    @property
    def description(self):
        return self.__description

    ## Factorisation code vérification regex
    @staticmethod
    def _check_regex(value : str, nom : str = "nom"):
        if re.match("^[A-Za-z\- éèêëîïûüçâäôö]{2,20}$", value):
            return value
        else:
            raise AttributeError(f"Votre {nom} ne doit pas contenir de caractères spéciaux")
    

    ## Méthode setter pour changer la valeur des attributs privés
    @nom.setter
    def nom(self, value : str):
        self.__nom = main.Player._check_regex(value)
    
    @date.setter 
    ## Utiliser Union (soit l'un ou l'autre) ===> date avec l'heure (intervalle date début - date de fin) ==> mettre 2 propriétés
    def date(self, value : str):
        ## Vérification format de date
        if isinstance(value, str) :
            try:
                dob = datetime.date.fromisoformat(value)
            except ValueError:
                raise ValueError("Format de date incorrect : veuillez renseigner sous cette forme AAAA-MM-JJ")
        
            today = date.today()

    @players.setter
    def players(self, value: list[Union[main.Player, int]]):
        pass
tournoi1 = Tournament("arizona", "USA", "2010-06-16", "data4", "data5", "data6", "data7", "data8")