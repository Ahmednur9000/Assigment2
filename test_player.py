import unittest
import player
import dice

class TestPlayerclass (unittest.TestCase):
    
    #test if a player obj will be intialized
    
    def test__init__player__obj(self):
        person_obj1 = player.Player("Ahmednuur")
        expected_name = person_obj1.name
        self.assertEqual(expected_name , "Ahmednuur")
    
    def test_update_score_1(self):
        person_obj2 = player.Player("Ahmednuur")
    
        person_obj2.update_score(1)
        
        exp = person_obj2.total_score
        
        self.assertEqual(exp , 0)
        
    def test_update_score_anyothervalue (self):
        person_obj3 = player.Player("Ahmednuur")
        
        person_obj3.update_score(5)
        
        exp = person_obj3.total_score
        
        self.assertEqual(exp , 5)
        
        
    def test_won_method(self):
        person_obj = player.Player("Meenu")
        
        expected_intial_winns = person_obj.get_wins()
        
        expected_intital_gameplayed = person_obj.get_gameplayed()
        
        person_obj.won()
        
        new_expected_wins = person_obj.get_wins()
        new_expected_gameplayed = person_obj.get_gameplayed()
        
        self.assertEqual(new_expected_wins , expected_intial_winns + 1)  
        self.assertEqual(new_expected_gameplayed , expected_intital_gameplayed + 1)
        
        
        
if __name__ ==  '__main__':
    unittest.main()
    