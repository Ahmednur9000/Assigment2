import random 


class player: 
    game_number = 1
    def __init__(self , name): 
        self.name = name  
        self.score = 0 
        self.PlayerId = self.randomPlayerId()
        self.game_played = 0
    
    def get_GamePlayed (self):
        return self.game_played
        
    def play_game (self):
        self.game_played += 1
    
    def get_Score (self):
        return self.score
        
    def randomPlayerId (self):
        return random.randint(1000 , 9999)
    
    def get_name(self):
        return self.name
    
    def set_name (self , changed_name):
        self.name = changed_name
    
    def roll_dice(self, dice):
        return dice.roll