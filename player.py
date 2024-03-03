import dice
class Player:
    
    def __init__(self , name):
        self.name = name 
        self.points = 0
        self.turn_score = 0
        self.gamewon = 0 
        self.gameloss = 0 
        
    def change_name (self , new_name):
        self.name = new_name
        
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
    
    def get_score(self):
        return self.points
    
    
    
    # 
    
     def save_players_list(self):
        with open(self.__filename, 'a+b') as file: 
            pickle.dump(self.__players, file)

    def load_players_list(self):
        with open(self.__filename, 'rb') as file:  
            self.__players == pickle.load(file)

    def create_player (self, p_name):
        if p_name in self.__players :
            print ("Name already taken. Please select another name.")
            return True  # Indicate that name is already taken
        else:
            self.__players.append(p_name)
            print ("Player created.")
            return False   # Indicate that name is available & player created.
            
    def search_player(self, p_name):       
        if p_name not in self.__players :
            print("Please enter correct name.")
            return True  
        else:
            return False   # Indicate that name is available # print("Enter correct name: ")
                 
        
    def change_name (self, orig_name, new_name):
        if orig_name in self.__players and new_name not in self.__players:
            self.__players.remove (orig_name)
            self.__players.append (new_name)
            print ("Name changed successfully.")
        elif orig_name in self.__players and new_name in self.__players:
            print ("Name already taken. Please select another name.")   
        else:
            print("Name does not exist. Select option 'Create New Player'.")
            
            
    def play (self, ):
        print ("Press Enter to roll.")
        print ("k")
        pass
        
        
    def score (self, points):
        
        if roll_dice_num !=1: 
            total += roll_dice_num
            self.__score += total
            return self.__score
        else :
            return self.__score
        
        
    def __str__(self):
        return f'The Player Name is {self.__name}, {self.__playerID}, {self.__score}'    