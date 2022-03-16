#test module for card deck

import unittest

import card_deck as cd

class TestCardDeck(unittest.TestCase):

    def test_card_builder(self):

        result = len(cd.CardBuilder.card_builder())
        self.assertEqual(result , 52)

if __name__ == '__main__':
    unittest.main()

#src\card_deck.py