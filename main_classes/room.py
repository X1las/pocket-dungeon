from main_classes.level import Level
from data._preferences import ROOM_SIZE, ROOM_DEFAULT_COLOR, TILE_SIZE
import pygame as pg


class Room:

    size = ROOM_SIZE*TILE_SIZE
    color = ROOM_DEFAULT_COLOR
    contains = []

    def __init__(self, level: Level, type: str = "DEFAULT", position=[0, 0]):

        self.level = level
        self.position = position
        self.roomType = "DEFAULT"
        self.level.contains.append(self)
        self.game = level.game

    # Room Update Loop
    def update(self):
        pass

    def draw(self):
        pg.draw.rect(self.game.screen, self.color,
                     pg.Rect(
                         self.position[0]-self.size/2,
                         self.position[1]-self.size/2,
                         self.size,
                         self.size))

        # For drawing Containables
        for i in self.contains:
            try:
                i.draw()
            except:
                self.game.sendMessage("ERR",
                                      "Object does not contain draw()",
                                      self)

    def roomGenerate(self):
        pass
