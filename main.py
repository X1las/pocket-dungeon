from main_classes.item import Item
from main_classes.game import Game
from main_classes.level import Level


g = Game(failsafe=False, running=True)
l1 = Level(g)

player = Item(game=g, level=l1, type="PLAYER", name="jkhjhlk", generate=False)

hat = Item(game=g, level=l1, type="HAT", name="Tattered Cowl", parent=player)
gloves = Item(game=g, level=l1, type="GLOVE", name="Worm Glove", parent=player)
boots = Item(game=g, level=l1, type="BOOT", name="Worm Boots", parent=player)
sword = Item(game=g, level=l1, type="SWORD", name="Rusty Sword", parent=player)
shield = Item(game=g, level=l1, type="SHIELD",
              name="Busted Shield", parent=player)


enemy = Item(game=g, level=l1, type="ENEMY", name="Bob")

g.run()
g.stop()
