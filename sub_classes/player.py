from main_classes.item import Item


class Player(Item):

    def __init__(self, name = "Dodo", position = (0,0)):
        self.name = name
        self.contains = []
        self.pos = position

    def takeDamage(self, part, damage):
        try:
            for i in self.contains:
                i.takeDamage()
        except:
            print("end of damage")

