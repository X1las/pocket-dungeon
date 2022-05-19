from main_classes.game import Game


class Level:
    
    def __init__(self, game:Game,rooms:int = None,levelType:str = None):
        self.game = game
        self.rooms = rooms
        self.levelType = levelType
        