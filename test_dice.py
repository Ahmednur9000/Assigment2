import dice
import unittest
 
class TestDiceClass(unittest.TestCase):
    
    def test__init__dice_object (self): 
       die = dice.Dice()
       
       
       self.assertIsInstance(die , dice.Dice)
       
       
        
    def test_roll_dice (self): 
        dice_obj= dice.Dice()
        res = dice_obj.roll()
        exp = 1 <= res <= 6
        
        self.assertTrue(exp)
        
if __name__ ==  '__main__':
    unittest.main()