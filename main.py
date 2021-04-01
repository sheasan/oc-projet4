import datetime
from datetime import date
import string

class Player:
    """test docstring"""
    ## Initialisation avec méthode spéciale __init__
    def __init__(self, nom, prenom, date_de_naissance, classement):
        self.__nom = nom
        self.__prenom = prenom
        self.__date_de_naissance = date_de_naissance
        self.__classement = classement
    
    ## Méthode get pour accèder aux attributs privés
    def _get_nom(self):
        return self.__nom

    def _get_prenom(self):
        return self.__prenom

    def _get_date_de_naissance(self):
        return self.__date_de_naissance
    
    def _get_classement(self):
        return self.__classement
    
    ## Méthode setter pour changer la valeur des attributs privés
    def _set_nom(self, nom):
        if len(nom) < 2 or len(nom) > 50:
            print("Le nombre de charactères doit être compris entre 2 et 50")
        elif any(char in (set(string.punctuation)) for char in nom):
            print("Votre nom ne doit pas contenir de charactères spéciaux")
        else:
            self.__nom = nom
    
    def _set_prenom(self, prenom):
        if len(nom) < 2 or len(nom) > 50:
            print("Le nombre de charactères doit être compris entre 2 et 50")
        elif any(char in (set(string.punctuation)) for char in prenom):
            print("Votre prénom ne doit pas contenir de charactères spéciaux")
        else:
            self.__prenom = prenom
    
    def _set_date_de_naissance(self, date_de_naissance):
        ## Vérification format de date
        try:
            dob = datetime.datetime.strptime(date_de_naissance, "%d/%m/%Y")
        except ValueError:
            print("Format de date incorrect : veuillez renseigner sous cette forme jj/mm/aaaa")
        
        ## Calcul de l'âge
        def calculate_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
        age = calculate_age(dob)

        ## Vérification de l'âge minimum requis
        if age < 12 :
            print("Vous devez avoir au moins 12 ans")
        else:
            self.__date_de_naissance = date_de_naissance
        
        
    
    def _set_classement(self, classement):
        if type(classement) != int:
            print("Veuillez entrer une donnée au format numéraire")
        elif classement < 0 or classement > 50:
            print("Veuillez entrer un nombre compris entre 0 et 50")
        else:
            self.__classement = classement
    
    def __repr__(self):
       return "Nom: "+self.__nom+" "+","+"Prénom: "+self.__prenom+", "+"Date de naissance: "+str(self.__date_de_naissance)+" ,"+"Classement: "+str(self.__classement)

    nom = property(_get_nom, _set_nom)
    prenom = property(_get_prenom, _set_prenom)
    date_de_naissance = property(_get_date_de_naissance, _set_date_de_naissance)
    classement = property(_get_classement, _set_classement)


player1 = Player("snow", "jon", "12/11/2000", 5)
player1.nom = "K"
player1.date_de_naissance = "12/03/2020"
player1.classement = 51
print(player1)
