import random 
import Dice


class Player: 
    
    def __init__(self , name): 
        self.name = name  
        self.score = 0 
        self.PlayerId = Player.randomPlayerId 
        
    def randomPlayerId (self):
        return random.randint(1000 , 9999)
    
    def get_name(self):
        return self.name
    
    def set_name (self , changed_name):
        self.name = changed_name
    
    def roll_dice(self, dice):
        player_roll = dice.roll