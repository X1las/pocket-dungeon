# Level Class, creates and manages rooms for a level

import math
import random
from main_classes.game import Game
from main_classes.room import Room
from data._preferences import EXPANSION, LEVEL_SIZE


class Level:

    contains = []
    rooms: dict = {}

    # Constructor, requires a Game object to function
    def __init__(self, game: Game, levelType: str = None, progress: int = 0,
                 generate: bool = True, name: str = "Level"):

        self.game = game
        self.levelType = levelType
        self.progress = progress
        self.game.contains.append(self)
        self.expansion = EXPANSION
        self.levelSize = LEVEL_SIZE
        self.name = name

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
        self.levelSize += EXPANSION

        variationRange = math.ceil(self.levelSize/10)
        variation = random.randint(-variationRange, variationRange)
        tempsize = self.levelSize + variation

        self.roomGen(tempsize, (0, 0))

    # Function that iterates the level to the next
    def nextLevel(self):
        self.rooms = None
        self.progress += 1
        self.generateLevel()

    def roomGen(self, rooms: int, startcoor: tuple):

        r = rooms
        coor = str(startcoor)

        if coor in self.rooms:
            r += 1
        else:
            print("Generating Room!")
            self.rooms[coor] = Room(level=self, position=startcoor)
        r += -1

        if rooms > 0:
            expand = False
            neighbors = [(1 + startcoor[0], 0 + startcoor[1]), 
                         (-1 + startcoor[0], 0 + startcoor[1]),
                         (0 + startcoor[0], 1 + startcoor[1]), 
                         (0 + startcoor[0], -1 + startcoor[1])]

            expanded = random.choice(neighbors)

            for i in neighbors:

                if str(i) in self.rooms:
                    neighbors.remove(i)
                else:
                    expand = True

            if expand:
                expanded = random.choice(neighbors)

            self.roomGen(r, expanded)
        else:
            self.game.sendMessage("LOG", "Level generation completed", self)
