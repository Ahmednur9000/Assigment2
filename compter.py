import dice
import random
class Computer: 
    
    def __init__(self ):
        self.name = "Mister Robot"
        self.total_score = 0
        self.turn_score = 0
        self.gamewon = 0 
        self.gameloss = 0 
        
    
    
    def update_score(self, roll_dice_num):
        
        if roll_dice_num == 1: 
            self.__totalscore = 0 
            
        else:
            self.__totalscore += roll_dice_num
            
    def won (self):
        self.__wins += 1
        self.__gameplayed += 1
    
    def lost(self):
        self.__loss += 1
        self.__gameplayed += 1
        
        
    def easyMode(self):
        die = dice.Dice
        rolled_dice = die.roll_computer_easyMode()
        return rolled_dice
        
    
    def mediumMode (self):
        option = random.randit(1 , 2)
        if option == 1 : 
            action1 = "h" # the computer holds
            return action1
        else:
            action2 = "r" # the computer roll the dice
            return action2
    
    def hardMode (self, score):
        strategy = random.randint(1,3)   
    # Strategy 1 = "Hold at 20", Strategy 2 = "Hold at 25", Strategy 3 = "Fair Play"
        if strategy == 1:
             if score < 20:
                return self.__option == 'r'
             else:
                 return self.__option == 'h'
        elif strategy == 2:
             if score < 25:
                return self.__option == 'r'
             else:
                 return self.__option == 'h'
        else :
             random_option = random.choice (['r', 'h'])
             return random_option        
        
        
        
        
    #     self.__comp_score = 0
    #     self.__option = ''
    #     if isinstance(comp, Player):
    #         self.__comp = comp
    #     else:
    #         raise ValueError("The 'comp' parameter must be an instance of Player.")

    
    # def score (self, roll_dice_num):
    #     total=0
    #     if roll_dice_num !=1: 
    #         total += roll_dice_num
    #         self.__score += total
    #         return self.__comp_score
    #     else :
    #         return self.__comp_score
        
    
    # def Beginner(self, score):
    #     strategy = random.randint(1,3)   # Strategy 1 = "Hold at 20", Strategy 2 = "Hold at 25", Strategy 3 = "Fair Play"
    #     if strategy == 1:
    #         if score < 20:
    #             return self.__option == 'P'
    #         else:
    #             return self.__option == 'H'
    #     elif strategy == 2:
    #         if score < 25:
    #             return self.__option == 'P'
    #         else:
    #             return self.__option == 'H'
    #     else :
    #         hold_play = random.choice (['H', 'P'])
    #         return hold_play
            
            
    # def Advance (self, score, opponent_score):
        
    #     if self.__comp_score == 0 and opponent_score == 0 :
    #         self.__option == 'P'
    #         if score < 20:
    #             return self.__option == 'P'
    #         else:
    #             return self.__option == 'H'
    #     elif self.__comp_score >= 25 :
    #         target_score = 100 - opponent_score
         
    #         return self.__option == 'H'
    #         return self.turn_total < target_score / num_turns
    #     #End race or keep race
    #     elif self.__comp_score > 71 or p1_score > 71 :
    #         return self.__option == 'P'
    #     else:
    #         diff_bet_scores = 21 + (self.__comp_score - p1_score)/8
            
            
        
    #     option = random.randint(1,2)
    #     hold_play = random.choice (['H', 'P'])
    #     if option == 1:
    #         if score < 25:
    #             return self.__option == 'P'
    #         else:
    #             return self.__option == 'H'
    #     else:
    #         if score < 25:
    #             return self.__option == 'P'
    #         else:
    #             return self.__option == 'H'