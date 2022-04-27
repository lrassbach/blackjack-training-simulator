#Test for dealer class

import unittest

import dealer

class TestDealer(unittest.TestCase):

    def test_deal_card(self):
        #arrange
        num_players = 1
        table_deck = ['Ace of Diamonds','Ten of Hearts','9 of Clubs','6 of Spades', '4 of Diamonds', '3 of Clubs']
        #act
        dealer_hand, hand, table_deck = (dealer.Dealer.deal_card(table_deck,num_players))
        result1 = dealer_hand
        result2 = hand
        result3 = table_deck
        #assert
        self.assertEqual(result1 , ['Ace of Diamonds', '9 of Clubs'])
        self.assertEqual(result2, ['Ten of Hearts','6 of Spades'])


if __name__ == '__main__':
    unittest.main()

#src\dealer.py