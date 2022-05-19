## Shared Functions
from main_classes.game import Game
from settings import TYPES

# Checks if a given type is one of the available types listen in settings
def typeCheck(type:str):
        check = False
        for i in TYPES:
            if type == i:
                check = True
        
        if check:
            return True
        else:
            return False
        
# Sends a message to the game object of a certain message type
def gameMessage(game:Game, msgType:str, msg:str):
    game.messages.append(msg + ">" + msgType)