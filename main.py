from main_classes.item import Item
from main_classes.game import Game
from main_classes.level import Level
from main_classes.room import Room
from sub_classes.player import Player


g = Game(failsafe=False, running=True)
l1 = Level(g)

player = Player(game=g, level=l1)

hat = Item(game=g,
           level=l1,
           type="HAT",
           name="Tattered Cowl",
           parent=player)

gloves = Item(game=g,
              level=l1,
              type="GLOVE",
              name="Worsm Glove",
              parent=player)

boots = Item(game=g,
             level=l1,
             type="BOOT",
             name="Worm Boots",
             parent=player)

sword = Item(game=g,
             level=l1,
             type="SWORD",
             name="Rusty Sword",
             parent=player)

shield = Item(game=g,
              level=l1,
              type="SHIELD",
              name="Busted Shield",
              parent=player)

enemy = Item(game=g,
             level=l1,
             type="ENEMY",
             name="Bob")

g.run()
g.stop()
