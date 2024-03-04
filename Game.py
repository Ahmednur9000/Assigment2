import dice
import player
import compter
import os
import random

class Game:
 
    def __init__(self):
        self._player_object_list = []
        self.current_player_index = 0
        self._point_score = 0
        self.target_score = 100
    
    
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
             
    def hold(self): 
        current_player = self._player_object_list[self.current_player_index]
        current_player.update_score(self._point_score)
        self._point_score = 0
        self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
             
    def Play_game (self ):
        
        while True:
            
            for players in self._player_object_list:
                if isinstance (players , player.Player):
                    
                    action = input("Roll again (r) or hold (h)? ")

                    if action.lower() == "r":
                        roll_result = dice.Dice.roll # Call the rollDice method to get the rolled number
                        if roll_result == 1:
                            print("You rolled a 1. Turn over.")
                            player.update_score(roll_result)  # Update the score (which will be 0 if it's 1)
                        else:
                            print(f"You rolled a {roll_result}.")
                            player.update_score(roll_result)
                            print(f"Current turn score: {player._Player__totalscore}")

                        if player._Player__totalscore >= self.target_score:
                            player.won()
                            
                            print(f"{player.name} wins with a score of {player._Player__totalscore}!")
                            return  # Exit the function, ending the game
                        
                        else:
                            player.lost()
                            return
                            
                               

                    elif action.lower() == "h":
                        print(f"{player.name} holds.")
                        self.hold()
                        
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
                            roll_result = compter.Computer.easyMode() # Call the rollDice method to get the rolled number
                            if roll_result == 1:
                                print("You rolled a 1. Turn over.")
                                compter.update_score(roll_result)  # Update the score (which will be 0 if it's 1)
                            else:
                                print(f"You rolled a {roll_result}.")
                                compter.update_score(roll_result)
                                print(f"Current turn score: {player._Player__totalscore}")

                            if compter._Player__totalscore >= self.target_score :
                                compter.won()
                                player.lost()
                                print(f"{compter.name} wins with a score of {compter.total_score}!")
                                return  # Exit the function, ending the game
                            elif player.get_total_score() >= self.target_score:
                                player.won()
                                compter.lost()
                                print(f"{player.name} wins with a score of {player.get_total_score()}!")
                                return  # Exit the function, ending the game

                        elif action.lower() == "h":
                            print(f"{compter.name} holds.")
                            self.hold()
                            
                    if choice == 2:
                        action = compter.Computer.mediumMode()
                        if action.lower() == "r":
                            roll_result = dice.Dice.roll() # Call the rollDice method to get the rolled number
                            if roll_result == 1:
                                print("You rolled a 1. Turn over.")
                                compter.update_score(roll_result)  # Update the score (which will be 0 if it's 1)
                            else:
                                print(f"You rolled a {roll_result}.")
                                compter.update_score(roll_result)
                                print(f"Current turn score: {player._Player__totalscore}")

                            if compter._Player__totalscore >= self.target_score:
                                compter.won()
                                player.lost()
                                print(f"{compter.name} wins with a score of {compter._Player__totalscore}!")
                                return  # Exit the function, ending the game
                            elif player.get_total_score >= self.target_score:
                                player.won
                                compter.lost
                                print(f"{player.name} wins with a score of {player.get_total_score()}!")
                                return # Exit the function, ending the game
                        
                        elif action.lower() == "h":
                            print(f"{compter.name} holds.")
                            self.hold()
                            
                    if choice == 3: 
                        score = dice.Dice.roll()
                        action = compter.Computer.hardMode(score)
                        if action.lower() == "r":
                            roll_result = dice.Dice.roll() # Call the rollDice method to get the rolled number
                            if roll_result == 1:
                                print("You rolled a 1. Turn over.")
                                compter.update_score(roll_result)  # Update the score (which will be 0 if it's 1)
                            else:
                                print(f"You rolled a {roll_result}.")
                                compter.update_score(roll_result)
                                print(f"Current turn score: {player._Player__totalscore}")

                            if compter._Player__totalscore >= self.target_score:
                                compter.won()
                                player.lost()
                                print(f"{compter.name} wins with a score of {compter._Player__totalscore}!")
                                return  # Exit the function, ending the game
                            elif player.get_total_score >= self.target_score:
                                player.won
                                compter.lost
                                print(f"{player.name} wins with a score of {player.get_total_score()}!")
                                return  # Exit the function, ending the game
                        
                        elif action.lower() == "h":
                            print(f"{compter.name} holds.")
                            self.hold()
