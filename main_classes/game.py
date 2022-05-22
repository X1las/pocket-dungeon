from data._preferences import RESOLUTION,FAILSAFE_TIME


class Game:
    
    resolution = RESOLUTION
    
    def __init__(self, running:bool = False, failsafe:bool = True, contains = [], uptime:int = 0):
        
        self.running = running
        self.contains = contains
        self.uptime = uptime
        
        if failsafe:
            self.failsafe = FAILSAFE_TIME
    
    def run(self):
        start = True
        print("Trying to start game...")
        
        if not self.running:
            print("'Running' has not been enabled, game will not run")
            
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
    
    def sendMessage(self, type:str, message:str, sender = None):
        objectfrom = ""
        if sender:
            objectfrom = sender
        if type == "ERR":
            print("Error: " + message + " from " + objectfrom.name)
        elif type == "LOG":
            print("Logging: " + message + " from " + objectfrom.name)
        else:
            print("Error: Trying to log incorrectly" )
        
                