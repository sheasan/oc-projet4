import datetime
from datetime import date
import string

class Player:
    """test docstring"""
    ## Initialisation avec méthode spéciale __init__
    def __init__(self, nom, prenom, date_de_naissance, classement):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.classement = classement
    
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
    
    ## Méthode setter pour changer la valeur des attributs privés
    @nom.setter
    def nom(self, nom):
        if len(nom) < 2 or len(nom) > 50:
            raise AttributeError("Le nombre de charactères doit être compris entre 2 et 50")
        elif any(char in (set(string.punctuation)) for char in nom):
            print("Votre nom ne doit pas contenir de charactères spéciaux")
        else:
            self.__nom = nom
    
    @prenom.setter
    def prenom(self, prenom):
        if len(prenom) < 2 or len(prenom) > 50:
            raise AttributeError("Le nombre de charactères doit être compris entre 2 et 50")
        elif any(char in (set(string.punctuation)) for char in prenom):
            print("Votre prénom ne doit pas contenir de charactères spéciaux")
        else:
            self.__prenom = prenom
    
    @date_de_naissance.setter
    def date_de_naissance(self, date_de_naissance):
        ## Vérification format de date
        try:
            dob = datetime.date.fromisoformat(date_de_naissance)
        except ValueError:
            print("Format de date incorrect : veuillez renseigner sous cette forme jj/mm/aaaa")
        
        today = date.today()
        
        age = today.year - dob.year

        ## Vérification de l'âge minimum requis
        if age < 12 :
            raise AttributeError("Vous devez avoir au moins 12 ans")
        else:
            self.__date_de_naissance = date_de_naissance
    
    @classement.setter
    def classement(self, classement):
        if not isinstance(classement, int):
            print("Veuillez entrer une donnée au format numéraire")
        elif classement < 0 or classement > 50:
            print("Veuillez entrer un nombre compris entre 0 et 50")
        else:
            self.__classement = classement
            
    def __repr__(self):
       return "Nom: "+self.nom+" "+","+"Prénom: "+self.prenom+", "+"Date de naissance: "+str(self.date_de_naissance)+" ,"+"Classement: "+str(self.classement)



player1 = Player("ut", "jon", "2018-06-18", 5)
##player1.nom = "Kaa"
##player1.date_de_naissance = "2020-06-13"
##player1.classement = 51
print(player1)
