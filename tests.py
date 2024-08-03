import unittest
from main import *


#write tests for:
#main menu/new/load game


class TestGameStart(unittest.TestCase):
    def test_new_story(self, mock_input):
        result = game_start()
        self.assertEqual(result, "New")
    
    def test_continue_story(self, mock_print, mock_input):
        result = game_start()
        self.assertEqual(result, "Continued story of Knight")
    

    def test_leave(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            game_start()



class TestCharacter_Validator

#combat






#combat






#combat





#combat






#combat





#combat






#combat




class TestHealSpell(unittest.TestCase):
    def test_heal_spell_increase_hp(self):
        Characters.char_maxhp = 30
        heal_spell()
        self.assertEqual(Characters.char_maxhp, 45)
    
    def test_heal_spell_no_increase(self):
        Characters.char_maxhp = 45
        heal_spell()
        self.assertEqual(Characters.char_maxhp, 45)
    
    def test_heal_spell_edge_case(self):
        Characters.char_maxhp = 40
        heal_spell()
        self.assertEqual(Characters.char_maxhp, 45)

class TestEnvironmental(unittest.TestCase):

    def test_environmental(self):
        random.seed(0)
        result = environmental()
        self.assertIn(result, ["plains", "mountains", "desert", "arctic", "forest"])
    
    



if __name__ == '__main__':
    unittest.main()