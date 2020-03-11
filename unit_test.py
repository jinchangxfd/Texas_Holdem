import unittest

from Texas_Holdem import poker_hand,who_win


class TestMethods(unittest.TestCase):
    def test_poker_hand(self):
        self.assertEqual(['High Card', 'J', 'T', '9', '7', '2'],
                         poker_hand([['2', 'H'], ['7', 'D'], ['J', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertEqual(['Pair', '7', 'J', 'T', '9'],
                         poker_hand([['7', 'H'], ['7', 'D'], ['J', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertEqual(['Two Pairs', '9', '7', 'T'],
                         poker_hand([['7', 'H'], ['7', 'D'], ['9', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertEqual(['Three of a Kind', '7'],
                         poker_hand([['7', 'H'], ['7', 'D'], ['7', 'S'], ['9', 'H'], ['T', 'H']]))
        self.assertEqual(['Straight', 'T'], poker_hand([['6', 'H'], ['7', 'D'], ['8', 'H'], ['9', 'H'], ['T', 'H']]))
        self.assertEqual(['Flush', 'J', 'T', '8', '7', '6'],
                         poker_hand([['6', 'H'], ['7', 'H'], ['8', 'H'], ['T', 'H'], ['J', 'H']]))
        self.assertEqual(['Full House', '7'], poker_hand([['6', 'H'], ['6', 'D'], ['7', 'S'], ['7', 'H'], ['7', 'C']]))
        self.assertEqual(['Four of a kind', '7'],
                         poker_hand([['6', 'H'], ['7', 'D'], ['7', 'S'], ['7', 'H'], ['7', 'C']]))
        self.assertEqual(['Straight flush', 'T'],
                         poker_hand([['6', 'H'], ['7', 'H'], ['8', 'H'], ['9', 'H'], ['T', 'H']]))

    def test_who_win(self):
        self.assertEqual('White wins', who_win('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH'))
        self.assertEqual('Black wins', who_win('Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S'))
        self.assertEqual('Black wins', who_win('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH'))
        self.assertEqual('Tie', who_win('Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH'))

if __name__ == '__main__':
    unittest.main()
