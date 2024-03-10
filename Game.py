import os
import time
import dice
import player
import compter
import random
import History

class Game: 
    
    History_obj = History.History_players()
    die = dice.Dice()
    
    def __init__(self):
        self._player_object_list = []
        self.current_player_index = 0
        self._point_score = 0
        self.target_score = 100
    
    def game_rules(self): 
        print("WELCOME ! \n")
        print("PIG : DICE GAME \n" )
        print("The Game Rules: \n") 
        
        print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\": " ) 
        print("-> If the player rolls a 1, they score nothing and it becomes the next player's turn.\n")
        print("->If the player rolls any other number, it is added to their turn total and the player's turn continues.\n")
        print("->If a player chooses to \"hold\", their turn total is added to their score, and it becomes the next player's turn. \n")
        print("The first player to score 100 or more points wins.")
        time.sleep(10)
        os.system("cls")
    
    
    def add_player_obj(self, player_obj):
        if isinstance(player_obj, player.Player) or isinstance(player_obj, compter.Computer):
            self._player_object_list.append(player_obj)
        else:
            print("Invalid player object type.")
            
        
    def roll_first (self, list_player_objs):
         a= random.choice(['Heads', 'Tails'])
         if a == 'Heads':
             print("P1 will roll first" + list_player_objs[0].name)
         else:
             print("P1 will roll first" + list_player_objs[1].name)
 
             
    def Play_game (self ):
        die = dice.Dice()
        computer_dice = compter.Computer()
        
        previous_player_index = None  
        
        while True:
            current_player = self._player_object_list[self.current_player_index]
            for players in self._player_object_list:
                if isinstance (players , player.Player):
                    
                    action = input("Roll again (r) or hold (h)? ")

                    if action.lower() == "r":
                        
                        roll_result = die.roll# Call the rollDice method to get the rolled number
                        if roll_result == 1:
                            print("You rolled a 1. Turn over.")
                            current_player.update_score(roll_result)
                            self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                        else:
                            print(f"You rolled a {roll_result}.")
                            current_player.update_score(roll_result)
                            print(f"Current turn score: {player._Player__totalscore}")

                        if current_player._Player__totalscore >= self.target_score:
                            current_player.won()
                            
                            print(f"{current_player.name} wins with a score of {player._Player__totalscore}!")
                            break  # Exit the function, ending the game
                        
                        else:
                            if previous_player_index is not None:
                                previous_player = self._player_object_list[previous_player_index]
                                previous_player.lost()
                            
                            break
                            
                               

                    elif action.lower() == "h":
                        print(f"{player.name} holds.")
                        self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                        
                        
                elif isinstance(players , compter.Computer()):
                    print(f"{players.name} turn: \n")
                    print("Choice difficulty level \n")
                    print("1. Easy Mode"
                              "2. Normal Mode"
                              "3. Hard Mode")
                    choice = input("Enter your choice: ")
                        
                    if choice == 1:
                        action = random.choice(["r", "h", "r", "r"])
                        if action.lower() == "r":
                            
                            roll_result = computer_dice.easyMode() # Call the rollDice method to get the rolled number
                            if roll_result == 1:
                                print("You rolled a 1. Turn over.")
                                current_player.update_score(roll_result) 
                                self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                            else:
                                print(f"You rolled a {roll_result}.")
                                current_player.update_score(roll_result)
                                print(f"Current turn score: {player._Player__totalscore}")

                            if current_player._Player__totalscore >= self.target_score :
                                
                                current_player.lost()
                                print(f"{compter.name} wins with a score of {compter.total_score}!")
                                return  # Exit the function, ending the game
                            elif current_player.get_total_score() >= self.target_score:
                                current_player.won()
                                
                                print(f"{player.name} wins with a score of {player.get_total_score()}!")
                                return  # Exit the function, ending the game
                            else:
                                if previous_player_index is not None:
                                    previous_player = self._player_object_list[previous_player_index]
                                    previous_player.lost()
                                    
                        elif action.lower() == "h":
                            print(f"{compter.name} holds.")
                            self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                            
                    if choice == 2:
                        action = compter.Computer.mediumMode()
                        if action.lower() == "r":
                            roll_result = dice.Dice.roll() # Call the rollDice method to get the rolled number
                            if roll_result == 1:
                                print("You rolled a 1. Turn over.")
                                compter.update_score(roll_result)
                                self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                            else:
                                print(f"You rolled a {roll_result}.")
                                compter.update_score(roll_result)
                                print(f"Current turn score: {player._Player__totalscore}")

                            if compter._Player__totalscore >= self.target_score:
                                compter.won()
                                player.lost()
                                print(f"{compter.name} wins with a score of {compter._Player__totalscore}!")
                                return  # Exit the function, ending the game
                            elif current_player.get_total_score >= self.target_score:
                                current_player.won
                        
                                print(f"{player.name} wins with a score of {player.get_total_score()}!")
                                return # Exit the function, ending the game
                        
                        elif action.lower() == "h":
                            print(f"{current_player.name} holds.")
                            self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                            
                    if choice == 3: 
                        score = dice.Dice.roll()
                        action = compter.Computer.hardMode(score)
                        if action.lower() == "r":
                            roll_result = dice.Dice.roll() # Call the rollDice method to get the rolled number
                            if roll_result == 1:
                                print("You rolled a 1. Turn over.")
                                current_player.update_score(roll_result) 
                                self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
                            else:
                                print(f"You rolled a {roll_result}.")
                                current_player.update_score(roll_result)
                                print(f"Current turn score: {player._Player__totalscore}")

                            if current_player._Player__totalscore >= self.target_score:
                               
                                player.lost()
                                print(f"{current_player.name} wins with a score of {current_player._Player__totalscore}!")
                                return  # Exit the function, ending the game
                            elif current_player.get_total_score >= self.target_score:
                                current_player.won
                                
                                print(f"{player.name} wins with a score of {player.get_total_score()}!")
                                return  # Exit the function, ending the game
                        
                        elif action.lower() == "h":
                            print(f"{compter.name} holds.")
                            self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
