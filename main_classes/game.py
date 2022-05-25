import sys
from data._preferences import RESOLUTION, FAILSAFE_TIME, GAME_NAME
import pygame as pg


class Game:

    # Class Variables
    resolution = RESOLUTION

    # Constructor
    def __init__(self, running: bool = False, failsafe: bool = True,
                 contains=[], uptime: int = 0):

        pg.init()
        pg.display.set_caption(GAME_NAME)

        self.running = running
        self.contains = contains
        self.uptime = uptime
        self.screen = pg.display.set_mode(RESOLUTION)
        self.failsafe = failsafe

    # Update
    def update(self):
        pass

    # Draw
    def draw():
        pass

    # Run function, starts the game loop
    def run(self):

        start = True
        print("Trying to start game...")

        # Checks if failsafe is enabled, and sets it to the failsafe timer for
        # automatic exit
        if self.failsafe:
            self.failsafe = FAILSAFE_TIME

        if self.running:

            while self.running:

                self.uptime += 1    # Tallies number of ticks

                # Sends a one time message that the game is running
                if start:
                    print("Game is Running!")
                    start = False

                # For executing stuff on game objects
                for i in self.contains:
                    try:
                        i.update()
                        i.draw()
                    except:
                        self.sendMessage(
                            "ERR",
                            "Object does not contain update() or draw()")

                # For terminating the game if the failsafe is enabled
                if self.failsafe:
                    if self.uptime == self.failsafe:
                        print("failsafe enabled...")
                        self.running = False

                # For handling pygame events
                for event in pg.event.get():
                    # only do something if the event is of type QUIT
                    if event.type == pg.QUIT:
                        # change the value to False, to exit the main loop
                        self.running = False
        else:
            print("'Running' has not been enabled, game will not run")

    # Logging function
    def sendMessage(self, type: str, message: str, sender=None):
        objectfrom = ""
        if sender:
            objectfrom = " -- From object: '" + sender.name + "'"
        if type == "ERR":
            print("Error: " + message + objectfrom)
        elif type == "LOG":
            print("Logging: " + message + objectfrom)
        else:
            print("Error: Trying to log incorrectly")

    # Stop function, ends pygame and terminates python process
    def stop(self):
        print("finished!")
        pg.quit()
        sys.exit()
