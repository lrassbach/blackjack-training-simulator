import card_deck as cd
import hand_evaluation as he
import unittest

class TestHandEvaluation(unittest.TestCase):
    def test_dealer_upcard(self):
        #arrange
        dealer_hand = ["Jack of Diamonds", "6 of Clubs"]
        #act
        dealer_up_value = he.HandEvaluation.dealer_upcard(dealer_hand)
        #assert
        self.assertEqual(6, dealer_up_value)
    
    def test_hand_value_sum(self):
        #arrange
        hand = ["2 of Spades", "7 of Hearts"]
        #act
        hand_value = he.HandEvaluation.hand_value_sum(hand)
        #assert
        self.assertEqual(9, hand_value)
    
    def test_hard_total_eval(self):
        #arrange
        hand_value =      [8,18,11,15,12,12,15,10,10,9,9]
        dealer_up_value = [0,0,0,5,3,5,8,8,10,8,5]
        action_list = []
        action_list_check = ['h','s','d','s','h','s','h','d','d','h','d']
        #act
        for i in range(11):
            action = he.HandEvaluation.hard_total_eval(hand_value[i],dealer_up_value[i])
            action_list.append(action)
        #assert
        self.assertListEqual(action_list_check,action_list)

    def test_soft_total(self):
        #arrange
        hand_value = [19,13,14,15,16,17,17,17,18,18,18]
        dealer_up_value = [9,5,8,6,3,4,7,10,8,4,9]
        action_list = []
        action_list_check =['s','d','h','d','h','d','s','h','s','s','h']
        #act
        for i in range (11):
            action = he.HandEvaluation.soft_total_eval(hand_value[i],dealer_up_value[i])
            action_list.append(action)
        #assert
        self.assertListEqual(action_list, action_list_check)

    def test_split_total_eval(self):
        #arrange
        hand_value = [4,4,6,6,8,10,10,12,12,14,14,16,18,18,20,22]
        dealer_up_value = [8,4,6,8,0,10,8,5,9,9,4,0,7,8,0,0]
        action_list = []
        action_list_check = ['h','sp','sp','h','h','h','d','sp','h','h','sp','sp','s','sp','s','sp']
        #act
        for i in range(16):
            action = he.HandEvaluation.split_total_eval(hand_value[i],dealer_up_value[i])
            action_list.append(action)
        #assert
        self.assertListEqual(action_list, action_list_check)

    def test_soft_hand(self):
        #arrange
        hand1 = ["Ace of Spades","4 of Clubs"]
        hand2 = ["Ace of Spades", "Ace of Diamonds"]
        #act
        tag1 = he.HandEvaluation.soft_check(hand1)
        tag2 = he.HandEvaluation.soft_check(hand2)
        #assert
        self.assertEqual(tag1, True)
        self.assertEqual(tag2, False)

    def test_split_check(self):
        #arrange
        hands = [["Ace of Hearts", "Ace of Spades"],["4 of Hearts","4 of Clubs"],["7 of Clubs", "5 of Diamonds"]]
        tags = []
        tag_check = [True, True, False]
        #act
        for item in range(3):
            tag = he.HandEvaluation.split_check(hands[item])
            tags.append(tag)
        #assert
        self.assertListEqual(tags,tag_check)

    def test_evaluation(self):
        #arrange
        dealer_hands = [["10 of Hearts", "9 of Clubs"], ["4 of Diamonds", "8 of Hearts"], ["5 of Diamonds", "4 of Spades"]]
        player_hands = [["Ace of Spades", "5 of Diamonds"], ["8 of Hearts", "8 of Clubs"], ["7 of Clubs", "4 of Hearts"]]
        #this test will iterate for 1 soft hand, 1 split hand, and 1 hard hand
        actions = []
        action_check =["h","sp","d"]
        #act
        for item in range(3):
            action = he.HandEvaluation.evaluation(player_hands[item],dealer_hands[item])
            actions.append(action)
        #assert
        self.assertListEqual(actions, action_check)
        

if __name__ == '__main__':
    unittest.main()
