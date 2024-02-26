import random

class dice:
    
    def __init__ (self): 
        self.sides = 6
        
    def roll (self): 
        rolled = random.randint(1 , self.sides)
        return rolled
        
# dice = Dice()

