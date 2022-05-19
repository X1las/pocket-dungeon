## Shared Functions

from settings import TYPES

# Checks if a given type is one of the available types listen in settings
def typeCheck(type:str):
        check = False
        for i in TYPES:
            if type == i:
                check = True
        
        if check:
            return True
        else:
            return False