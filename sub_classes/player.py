from main_classes.game import Game
from main_classes.item import Item
from main_classes.level import Level
from data._preferences import PLAYER_MOVEMENT, TILE_SIZE, PLAYER_SIZE
import pygame as pg


class Player(Item):

    width = PLAYER_SIZE*TILE_SIZE/2
    height = PLAYER_SIZE*TILE_SIZE
    keys = {"a": 0,
            "d": 0,
            "w": 0,
            "s": 0}

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
        self.position[0] += (self.keys["a"] + self.keys["d"]) * PLAYER_MOVEMENT
        self.position[1] += (self.keys["w"] + self.keys["s"]) * PLAYER_MOVEMENT

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
        if input.type == pg.KEYDOWN:
            if input.key == pg.K_s:
                self.keys["s"] = 1
                print("moved!")
            if input.key == pg.K_w:
                self.keys["w"] = -1
                print("moved!")
            if input.key == pg.K_a:
                self.keys["a"] = -1
                print("moved!")
            if input.key == pg.K_d:
                self.keys["d"] = 1
                print("moved!")

        if input.type == pg.KEYUP:
            if input.key == pg.K_s:
                self.keys["s"] = 0
            if input.key == pg.K_w:
                self.keys["w"] = 0
            if input.key == pg.K_a:
                self.keys["a"] = 0
            if input.key == pg.K_d:
                self.keys["d"] = 0
