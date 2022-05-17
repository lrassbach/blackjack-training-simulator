import card_deck as cd
import deck_positional_list as dp
import dealer
import players
import hand_evaluation
from ui import UI

class Main:
    
    def main():
        
        #this is going to be a while loop
        
        UI.welcome()
        print('------------------------------')
        card_deck_dictionary = cd.CardBuilder.card_builder_dict()

        card_deck_list = cd.CardBuilder.card_builder_list()
        
        deck_size = 6
        table_deck = dealer.Dealer.table_deck_builder(card_deck_dictionary, deck_size)
        play = True
        while play == True:
            comparison = True
            dealer_hand, hand, table_deck= dealer.Dealer.deal_card(table_deck, 1)
            UI.hand_display(dealer_hand,hand)
            d_blackjack_check = dealer.Dealer.check_blackjack(dealer_hand)
            p_blackjack_check = players.Players.check_player_blackjack(hand)
            if d_blackjack_check == True or p_blackjack_check == True:
                comparison = False
            if comparison == True:
                action = hand_evaluation.HandEvaluation.evaluation(hand, dealer_hand)
                choice = UI.get_user_action()
                check, quit = UI.action_check(choice, action)
            if quit == True:
                play = False
            print('------------------------------')
            print('------------------------------')
        print('Thanks for playing!')
            
Main.main()