class Computer: 
    
    def __init__(self ):
        self.name = "Mister Robot"
        self.points = 0
        self.turn_score = 0
        self.gamewon = 0 
        self.gameloss = 0 
        
        
    def update_score(self,score):
        self.points += score
        
    def rolldice ():
        die = dice.Dice()
        return die.roll
    
    def hold(self, score):
        self.update_score(score)
        self.turn_score = 0
        
    def winner (self):
        self.gamewon += 1
        
    def lost(self):
        self.gameloss += 1
     
    def get_name(self):
        return self.name
    
    def get_wins(self):
        return self.gamewon
    
    def get_losses(self):
        return self.gameloss
    
    # The stragies for easy , normal and hard 
    
    def easyMode ():
        pass
    
    def normalMode ():
        pass
    
    def hardMode ():
        pass
    