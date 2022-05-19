from main_classes.item import Item
from main_classes.game import Game

g = Game()

player = Item(game = g, type = "PLAYER", name = "DoDo")

hat = Item(game = g, type = "HAT", name = "Tattered Cowl", parent = player)
gloves = Item(game = g, type = "GLOVE", name = "Worm Glove", parent = player)
boots = Item(game = g, type = "BOOT", name = "Worm Boots", parent = player)
sword = Item(game = g, type = "SWORD", name = "Rusty Sword", parent = player)
shield = Item(game = g, type = "SHIELD", name = "Busted Shield", parent = player)


enemy = Item(game = g,type = "ENEMY", name = "Bob")


g.running = True
g.run()

print("finished!")