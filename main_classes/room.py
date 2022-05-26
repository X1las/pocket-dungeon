from main_classes.level import Level
from data._preferences import ROOM_SIZE



class Room:

    size = ROOM_SIZE

    def __init__(self, level: Level, type: str = None):
        self.level = level

        if not type:
            self.levelType = "DEFAULT"
        else:
            self.levelType = type

    def update(self):
        pass

    def draw(self):
        pass

    def roomGenerate(self):
        pass
