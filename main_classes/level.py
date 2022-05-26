# Level Class, creates and manages rooms for a level

from main_classes.game import Game
# from data._preferences import EXPANSION, LEVEL_SIZE


class Level:

    rooms = None
    contains = []

    # Constructor, requires a Game object to function
    def __init__(self, game: Game, levelType: str = None, progress: int = 0,
                 generate: bool = True):

        self.game = game
        self.levelType = levelType
        self.progress = progress
        self.game.contains.append(self)

        if generate:
            self.generateLevel()

    # Update loop
    def update(self):

        # For updating containables
        for i in self.contains:
            try:
                i.update()
            except:
                self.game.sendMessage("ERR",
                                      "Object does not contain update()",
                                      self)

    # Draw loop
    def draw(self):

        # For drawing Containables
        for i in self.contains:
            try:
                i.draw()
            except:
                self.game.sendMessage("ERR",
                                      "Object does not contain draw()",
                                      self)

    # Function that generates rooms for the level
    def generateLevel(self):
        pass

    # Function that iterates the level to the next
    def nextLevel(self):
        self.rooms = None
        self.progress += 1
        self.generateLevel()
