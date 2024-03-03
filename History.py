import player

class History_players:
    self.__player_data = {}
    self.__filename = "player_stats.bin"
    
    
    def addPlayer(self, player):
        if player.name in self.__player_data:
            self.__player_data[player.name].append((player.__wins, player.__loss))
        else:
            self.__player_data[player.name] = [(player.__wins, player.__loss)]

    def print_stats(self , player_object):
        if player_object in self.__player_data:
            for player_name, game_stats in self.__player_data.items():
                print("Player Name:", player_name)
                for wins, losses in game_stats:
                   print("Wins: ", wins)
                   print("Losses: ", losses)

    
    def save_players_data(self):
        with open(self.__filename, 'wb') as file:  # Use 'wb' for writing in binary mode
            pickle.dump(self.__player_data, file)

    def load_players_list(self):
        with open(self.__filename, 'rb') as file:  # Use 'rb' for reading in binary mode
            return self.__player_data == pickle.load(file)



    