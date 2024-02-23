import random

class dice:
    
    def __init__ (self , sides = 6 ): 
        self.sides = sides
        
    def roll (self): 
        self.rolled = random.randint(1 , self.sides)