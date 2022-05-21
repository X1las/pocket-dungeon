from main_classes.game import Game


class Level:
    
    rooms = None
    
    def __init__(self, game:Game, levelType:str = None, stage:int = 0, generate:bool = True):
        
        self.game = game
        self.levelType = levelType
        self.progress = stage
        
        if generate:
            self.generateLevel()
    
    # Function that generates the level
    def generateLevel(self):
        rooms = self.rooms
    
    # Function that iterates the level
    def nextLevel(self):
        self.rooms = None
        self.progress+=1
        self.generateLevel()  