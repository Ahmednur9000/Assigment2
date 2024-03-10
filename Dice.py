import random

class Dice:
    
    def __init__ (self): 
        self.sides = 6
        self.computer_easy_mode_option = [1, 1, 1, 1, 2, 3, 4, 5, 6]
        
    def roll (self): 
        rolled = random.randint(1 , self.sides)
        return rolled
    
    def roll_computer_easyMode(self):
        rolled  = random.choice(self.computer_easy_mode_option)
        return rolled
    
        
# dice = Dice()

if __name__ == "__main__":
    die = Dice()
    rolled_result = die.roll()
    print(rolled_result)
    