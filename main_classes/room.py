from level import Level

class Room:

    def __init__(self, level:Level, type:str = None):
        self.level = level
        
        if not type:
            self.levelType = "DEFAULT"
        else:
            self.levelType = type
            
    def roomGenerate():
        pass
        
