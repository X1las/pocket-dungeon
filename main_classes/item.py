from commons import typeCheck

class Item:

    # Class Variables:
    expansions:int = None
    slots:int = None
    health:int = None
    
    contains = []
    resources = []

    # Constructor, uses the game object itself for initialization
    def __init__(
        self, 
        game, 
        type:str, 
        parent = None, 
        name:str = "Newt",
        position:int = [0,0], 
        color:int = None):
        
        # Instanced Variables
        self.parent = parent
        self.name = name
        self.game = game
        self.color = color
        
        self.typeChange(type) # See function further down for more info
        
        # Checks if the item has a parent, and adds itself to the parent's list of containables if it has
        if self.parent:
            self.localpos = position
            self.position = self.parent.position + position
            self.parent.contains.append(self)
            self.gameMessage("LOG",self.name + " has been made child of object " + self.parent.name)
        else:
            self.position = position
    
    # Function to update 'health' based on the amount of citizens the item contains
    def updateHealth(self):
        if len(self.contains) != 0:
            self.health = 0
            for i in self.contains:
                self.total += i.citizens
    
    # Changes the type of the item to one listen in settings.py, or sends an error
    def typeChange(self, type: str):
        if typeCheck(type):
            self.type = type
        else:
            self.gameMessage("ERR","Cannot change type of object to '" + type)

    # Sends a message to the game object of a certain message type
    def gameMessage(self, msgType:str, msg:str):
        self.game.messages.append(msg + ">" + msgType)
    
    def resourceGenerate():
        
        pass
    
    def update():
        pass