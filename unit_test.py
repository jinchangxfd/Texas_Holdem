import unittest
from Texas_Holdem import poker_hand

class TestStringMethods(unittest.TestCase):
    def test_poker_hand(self):
        self.assertIs('High Card',poker_hand([['2', 'H'], ['7', 'D'], ['J', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertIs('Pair',poker_hand([['7', 'H'], ['7', 'D'], ['J', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertIs('Two Pairs',poker_hand([['7', 'H'], ['7', 'D'], ['9', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertIs('Three of a Kind',poker_hand([['7', 'H'], ['7', 'D'], ['7', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertIs('Straight',poker_hand([['6', 'H'], ['7', 'D'], ['8', 'H'], ['9', 'H'], ['T', 'H']]))
        self.assertIs('Flush',poker_hand([['6', 'H'], ['7', 'H'], ['8', 'H'], ['T', 'H'], ['J', 'H']]))
        self.assertIs('Full House',poker_hand([['6', 'H'], ['6', 'D'], ['7', 'S'], ['7', 'H'], ['7', 'C']]))
        self.assertIs('Four of a kind',poker_hand([['6', 'H'], ['7', 'D'], ['7', 'S'], ['7', 'H'], ['7', 'C']]))
        self.assertIs('Straight flush',poker_hand([['6', 'H'], ['7', 'H'], ['8', 'H'], ['9', 'H'], ['T', 'H']]))

if __name__ == '__main__':
    unittest.main()
