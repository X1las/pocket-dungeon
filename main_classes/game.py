from settings import RESOLUTION,FAILSAFE_TIME


class Game:
    
    resolution = RESOLUTION
    contains = []
    messages = []
    uptime = 0
    running = None
    failsafe = None
    
    def __init__(self, running = False, failsafe = True):
        self.running = running
        
        if failsafe:
            self.failsafe = FAILSAFE_TIME
    
    def run(self):
        start = True
        print("Trying to start game...")
        
        if not self.running:
            print("'Running' has not been enabled, game will not run")
            
        while self.running:
                
            self.uptime += 1
            self.resolveMessages()
            
            if start:
                print("Game is Running!")
                start = False
            
            for i in self.contains:
                i.update()
            
            if self.failsafe:
                if self.uptime == self.failsafe:
                    print("failsafe enabled...")
                    self.running = False
        
                
    def resolveMessages(self):
        if len(self.messages) != 0:
            for i in self.messages:
                obs = i.split(">")
                if obs[1] == "ERR":
                    print("ERROR: " + obs[0])
                if obs[1] == "LOG":
                    print("Logging: " + obs[0])
            self.messages = []
                