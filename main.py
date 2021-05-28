import player
import playermanager
import tournament
import json

try:
    player1 = player.Player("snow", "jon", "2000-06-18", 5, "Homme", 1)
    player2 = player.Player("boris", "klein", "2000-06-18", 5, "Homme")
    ##player2 = Player("boris", "klein", "2000-06-18", 5, "Homme", 1)
    print(player1)
    ## Ajout code serialization
    serialization = json.dumps(player2.__dict__)
    """with open( "datafile.json" , "w" ) as write:
        json.dump( serialization , write )"""
    print((serialization))
except AttributeError as nameError:
    print(nameError)