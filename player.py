import dice
class Player:
    
    def __init__(self , name):
        self.name = name 
        self.points = 0
        self.turn_score = 0
        self.gamewon = 0 
        self.gameloss = 0 
        
        
    
    def update_score(self, roll_dice_num):
        
        if roll_dice_num == 1: 
            self.__totalscore = 0 
            
        else:
            self.__totalscore += roll_dice_num
    
            
    def get_total_score (self):
        return self.__totalscore
    
    def won (self):
        self.__wins += 1
        self.__gameplayed += 1
    
    def lost(self):
        self.__loss += 1
        self.__gameplayed += 1
    