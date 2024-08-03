import unittest
import pytest
from unittest.mock import patch
from main import *

class testfunctions(unittest.TestCase):
    def test_heal_spell_increase_hp(self):
        Characters.char_maxhp = 30
        heal_spell()
        self.assertEqual(Characters.char_maxhp, 40)
    
    def test_heal_spell_no_increase(self):
        Characters.char_maxhp = 45
        heal_spell()
        self.assertEqual(Characters.char_maxhp, 45)
    1
    def test_heal_spell_edge_case(self):
        Characters.char_maxhp = 40
        heal_spell()
        self.assertEqual(Characters.char_maxhp, 45)
      

class TestEnvironmental(unittest.TestCase):

    def test_environmental(self):
        random.seed(0)
        result = environmental()
        self.assertIn(result, ["plains", "mountains", "desert", "arctic", "forest"])

    def test_environmental_advantage_player(self):
       Characters.char_type = "Wizard"
       Characters.char_atk = 14
       assert environmental_advantage_player("mountains") == 16

    def test_environmental_advantage_enemy(self):
       Enemies.enm_type = "undead"
       Enemies.enm_atk = 9
       assert environmental_advantage_enemy("desert") == 11



if __name__ == '__main__':
    unittest.main()