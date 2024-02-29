import player

class History_players:
    
    Player_data = {}

    def addPlayer(self, player):
        if player.name in self.Player_data:
            self.Player_data[player.name].append((player.get_winns(), player.get_losses()))
        else:
            self.Player_data[player.name] = [(player.get_winns(), player.get_losses())]

    def print_stats(self):
    
        for player_name, game_stats in self.Player_data.items():
            print("Player Name:", player_name)
            for wins, losses in game_stats:
                print("Wins: ", wins)
                print("Losses: ", losses)



    