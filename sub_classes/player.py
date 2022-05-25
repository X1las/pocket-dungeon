from main_classes.game import Game
from main_classes.item import Item
from main_classes.level import Level


class Player(Item):
    
    # Constructor, requires Game and level object
    def __init__(self,game:Game, level:Level):
        self.game = game
        self.level = level
    
    # Player Controller, manages input from the player
    def playerController(self):
        pass
    
    def update(self):
        pass