import sys
from data._preferences import RESOLUTION,FAILSAFE_TIME,GAME_NAME
import pygame as pg

class Game:
    
    resolution = RESOLUTION
    
    def __init__(self, running:bool = False, failsafe:bool = True, contains = [], uptime:int = 0):
        
        pg.init()
        pg.display.set_caption(GAME_NAME)
        
        self.running = running
        self.contains = contains
        self.uptime = uptime
        self.screen = pg.display.set_mode(RESOLUTION)
        self.failsafe = failsafe
    
    def run(self):
        start = True
        print("Trying to start game...")
        
        if self.failsafe:
            self.failsafe = FAILSAFE_TIME
        
        if self.running:
            
            while self.running:
                    
                self.uptime += 1
                            
                if start:
                    print("Game is Running!")
                    start = False
                
                for i in self.contains:
                    i.update()
                
                if self.failsafe:
                    if self.uptime == self.failsafe:
                        print("failsafe enabled...")
                        self.running = False
                
                for event in pg.event.get():
                    # only do something if the event is of type QUIT
                    if event.type == pg.QUIT:
                        # change the value to False, to exit the main loop
                        self.running = False
        else:
            print("'Running' has not been enabled, game will not run")
    
    def sendMessage(self, type:str, message:str, sender = None):
        objectfrom = ""
        if sender:
            objectfrom = " -- From object: '" + sender.name + "'"
        if type == "ERR":
            print("Error: " + message + objectfrom)
        elif type == "LOG":
            print("Logging: " + message + objectfrom)
        else:
            print("Error: Trying to log incorrectly" )
        
    def update(self):
        pass
    
    def stop(self):
        print("finished!")
        pg.quit()
        sys.exit()