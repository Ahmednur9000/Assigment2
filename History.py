from Player import player

#Contain a collection of player, prints its stats#
class Collection_History_players: 
    
    def __init__(self):
        
        self.Player_data = {}
        
    def addPlayer (self , player , score):
        if player in self.Player_data:
            self.Player_data[player.name].append((player.get_gameplayed() , score))
        else:
            self.Player_data[player.name] = [( player.get_GamePlayeda() ,score)]
        
    def print_stats(self):
            for player_name, game_scores in self.player_data.items():
                print("Player Name:", player_name)  
            
            for game_number, score in game_scores:
                print("Game_played: ", game_number)  
                print("Score: ", score)  
                
           
                