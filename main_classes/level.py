# Level Class, creates and manages rooms for a level

from main_classes.game import Game
from data._preferences import EXPANSION, LEVEL_SIZE


class Level:
    Rooms = None

    # Constructor, requires a Game object to function
    def __init__(self, game: Game, levelType: str = None, stage: int = 0,
                 generate: bool = True):

        self.game = game
        self.levelType = levelType
        self.progress = stage

        if generate:
            self.generateLevel()

    # Update loop
    def update(self):
        pass

    # Draw loop
    def draw(self):
        pass

    # Function that generates rooms for the level
    def generateLevel(self):
        diff = EXPANSION
        roomstemp = LEVEL_SIZE

    # Function that iterates the level to the next
    def nextLevel(self):
        self.rooms = None
        self.progress += 1
        self.generateLevel()
