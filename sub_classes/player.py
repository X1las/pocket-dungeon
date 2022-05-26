from main_classes.game import Game
from main_classes.item import Item
from main_classes.level import Level
from data._preferences import PLAYER_MOVEMENT
import pygame as pg


class Player(Item):

    width = 32
    height = 64

    # Constructor, requires Game and level object
    def __init__(self, game: Game,
                 level: Level,
                 position: int = [0, 0],
                 color: int = (255, 0, 0),
                 name: str = "Newt"):

        self.game = game
        self.level = level
        self.position = position
        self.color = color
        self.name = name
        self.game.player = self
        
        self.game.contains.append(self)

    # Player Update Loop
    def update(self):
        pass

    # Player Draw Loop
    def draw(self):
        pg.draw.rect(self.game.screen, self.color,
                     pg.Rect(
                         self.position[0]-self.width/2,
                         self.position[1]-self.height/2,
                         self.width,
                         self.height))

    # Player Controller, manages input from the game
    def playerController(self, input):
        if input == pg.K_s:
            self.position[1] += PLAYER_MOVEMENT
            print("moved!")
