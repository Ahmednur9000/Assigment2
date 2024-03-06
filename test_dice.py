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
        
    def test_roll_computer_roll(self):
        dice_obj = dice.Dice()
        res1 = dice_obj.roll_computer_easyMode()
        exp2 = 1 <= res1 <= 6
        
        self.assertTrue(exp2)
            
        
if __name__ ==  '__main__':
    unittest.main()