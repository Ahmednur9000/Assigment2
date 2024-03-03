import player

class Game:
        
 # Shuld handle the switching of player
 # Check if the player exits
    def __init__(self):
        self._player_object_list = []
        self.current_player_index = 0
        self._point_score = 0
        self.target_score = 100
    
    def add_list_playerObj (self, player_obj):
        if player_obj not in self._player_object_list:
            self._player_object_list.append(player_obj)
        
            
    def game_rules(self):    
        print("WELCOME ! \n")
        print("PIG : DICE GAME \n" )
        print("The Game Rules: \n") 
        print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\": \n" ) 
        print("-> If the player rolls a 1, they score nothing and it becomes the next player's turn.")
        print("-> If the player rolls any other number, it is added to their turn total and the player's turn continues.")
        print("-> If a player chooses to \"hold\", their turn total is added to their score, and it becomes the next player's turn. \n")
        print("The first player to score 100 or more points wins.")
        
        time.sleep(5)
        os.system("cls")
        
    def roll_first (self, p1_name, p2_name):
         a= random.choice(['Heads', 'Tails'])
         if a == 'Heads':
             print("P1 will roll first" + p1_name)
         else:
             print("P1 will roll first" + p2_name)
             
    def hold(self): 
        current_player = self._player_object_list[self.current_player_index]
        current_player.update_score(self._point_score)
        self._point_score = 0
        self.current_player_index = (self.current_player_index + 1) % len(self._player_object_list)
             
    def Play_game (self):
        self.game_rules()
        while True:
            for player in self._player_object_list:
                print(f"{player.name}'s turn:")
                action = input("Roll again (r) or hold (h)? ")

                if action.lower() == "r":
                    roll_result = player.rollDice()()  # Call the rollDice method to get the rolled number
                    if roll_result == 1:
                        print("You rolled a 1. Turn over.")
                        player.update_score(roll_result)  # Update the score (which will be 0 if it's 1)
                    else:
                        print(f"You rolled a {roll_result}.")
                        player.update_score(roll_result)
                        print(f"Current turn score: {player._Player__totalscore}")

                    if player._Player__totalscore >= self.target_score:
                        print(f"{player.name} wins with a score of {player._Player__totalscore}!")
                        return  # Exit the function, ending the game

                elif action.lower() == "h":
                    print(f"{player.name} holds.")
                    self.hold()
                    break

                # Check if any player has won after each turn
                if player._Player__totalscore >= self.target_score:
                    print(f"{player.name} wins with a score of {player._Player__totalscore}!")
                    return  # Exit the function, ending the game