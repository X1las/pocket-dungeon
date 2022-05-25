# Item Class, contains all the shared functionality of items and NPC's
# Uses data from _preferences.py, itemtypes.py and enemytypes.py

from main_classes.game import Game
from main_classes.level import Level
from data._preferences import ITEMTYPES


class Item:

    # Class Variables:
    expansions: int = None
    slots: int = None
    health: int = None

    contains = []
    resources = []

    # Constructor, requires both a game AND level object to be created.
    def __init__(
            self,
            game: Game,
            level: Level,
            type: str,
            parent=None,
            name: str = "Newt",
            position: int = [0, 0],
            color: int = [0, 0, 0],
            generate: bool = True):

        # Instanced Variables
        self.game = game
        self.level = level
        self.parent = parent
        self.name = name
        self.color = color
        self.typeChange(type)  # See function further down for more info

        if generate:
            self.resourceGenerate()

        # Checks if the item has a parent, and adds itself to containables
        if self.parent:
            self.localpos = position
            self.position = self.parent.position + position
            self.parent.contains.append(self)
            self.game.sendMessage(
                "LOG", self.name + " has been made child of object "
                + self.parent.name, self)
        else:
            self.position = position

    # Update loop
    def update(self):
        pass

    # Draw loop
    def draw():
        pass

    # Function to update an item's'health'
    def updateHealth(self):
        if len(self.contains) != 0:
            self.health = 0
            for i in self.contains:
                self.total += i.citizens

    # Changes the type of the item to one of the types in dict
    def typeChange(self, type: str):
        try:
            self.populationMax = ITEMTYPES[type]
            self.type = type
        except:
            self.game.sendMessage(
                "ERR", "Cannot change type of object to '"
                + type
                + "', assigning it to NONE", self)
            self.type = None

    # Generates random resources for the item
    def resourceGenerate(self):
        pass
