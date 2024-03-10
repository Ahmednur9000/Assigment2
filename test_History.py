import unittest
import sys
import history
import player
import io 

class TestHistory(unittest.TestCase):
    # def setup(self):
    #     self.History_obj = history.History()
    #     self.History_obj.__player_data = {"ahmed": [5, 3, 2] , "meenu": [8, 5, 3]}
        
        # self.History_obj.__history = 'History.pkl'
    def test_init_History(self):
        self.History_obj = history.History()
        self.assertIsInstance(self.History_obj , history.History)
        
        
        
        
    def test_add_new_player(self):
        self.History_obj2 = history.History()
        self.Player_obj = player.Player("Zamzam")
        self.Player_obj.count_of_games_played = 10
        self.Player_obj.wins = 4
        self.Player_obj.loss = 6
        self.History_obj2.addPlayer(self.Player_obj)
        
        exp = [10, 4, 6]
        
        dictionary = self.History_obj2.get_dictionary()
        
        value = dictionary.get("zamzam")
        
        self.assertEqual(value , exp)
        
    def test_add_already_existing_player(self):
        self.History_obj3 = history.History()
        self.Player_obj = player.Player("darkloard")
        self.Player_obj.count_of_games_played = 10
        self.Player_obj.wins = 4
        self.Player_obj.loss = 6
        self.History_obj3.addPlayer(self.Player_obj)
        
       
        
        self.Player_obj2 = player.Player("darkloard")
        self.Player_obj2.count_of_games_played = 5
        self.Player_obj2.wins = 3
        self.Player_obj2.loss = 2
        
        self.History_obj3.addPlayer(self.Player_obj2)
        
        dictionary = self.History_obj3.get_dictionary()
        
        Value = dictionary.get("darkloard")
        
        exp = [15, 7, 8]      
        
        self.assertEqual(Value, exp)
        
        
    # def test_print_stat(self):
        
    #     self.History_obj4 = history.History()
    #     self.Player_obj = player.Player("darkloard")
    #     self.Player_obj.count_of_games_played = 10
    #     self.Player_obj.wins = 4
    #     self.Player_obj.loss = 6
    #     self.History_obj4.addPlayer(self.Player_obj)
        
    #     captured_output = io.StringIO()
    #     sys.stdout = captured_output
        
    #     self.History_obj4.print_stats()
        
    #     printed_output = captured_output.getvalue()
        
    #     sys.stdout = sys.__stdout__
        
    #     expected_output = """"   
    #     Player Name        Counts    Wins      Losses
    #     ------------------------------------------------------------
    #     darkloard           10        4          6   
    #     ------------------------------------------------------------\n  
    #     """
        
    #     self.assertEqual(printed_output , expected_output)
        
    #     self.maxDiff = None
        
    def test_stats_update_name_change(self):
        self.History_obj4 = history.History()
        self.Player_obj = player.Player("Escanor")
        self.Player_obj.count_of_games_played = 10
        self.Player_obj.wins = 4
        self.Player_obj.loss = 6
        self.History_obj4.addPlayer(self.Player_obj)
        
        self.History_obj4.stats_update_name_change("Escanor" , "Lion")
        
        dictionary = self.History_obj4.get_dictionary()
        
        Value = dictionary.get("lion")
        
        exp = [10, 4, 6]
        
        self.assertEqual(Value , exp)
        
    def test_get_dictionary (self):
        self.History_obj5 = history.History()
        self.Player_obj = player.Player("escanor")
        self.Player_obj.count_of_games_played = 10
        self.Player_obj.wins = 4
        self.Player_obj.loss = 6
        self.History_obj5.addPlayer(self.Player_obj)
        
        rep = self.History_obj5.get_dictionary()
        
        exp = {"escanor": [10, 4, 6]}        
        
        self.assertEqual(rep , exp)