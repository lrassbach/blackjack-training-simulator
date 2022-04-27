#dealer class
import random
import card_deck
from players import Players
class Dealer:
        #this function puts together the table deck
        def table_deck_builder(card_deck_list, num_decks):
            ##UI will set input num_decks
            table_deck = []
            x = 0
            for item in range(int(num_decks)):
                for y in card_deck_list:
                    table_deck.append(y)
                x += 1
            random.shuffle(table_deck)    
            return table_deck

        def deck_length_check(table_deck):
            if len(table_deck) < (len(table_deck)/12):
                reshuffle = True
            else:
                reshuffle = False
            return reshuffle

        #This function deals cards and removes them from the deck
        def deal_card(table_deck, num_players):
            import players as players
            hand = players.Players.get_hand()
            dealer_hand = []
            x = 1
            for item in range(4):
                if x % 2 != 0:
                    card = table_deck.pop(x)
                    hand.append(card)
                    x += 1
                elif x % 2 == 0:
                    card = table_deck.pop(x)
                    dealer_hand.append(card)
                    x += 1
            return dealer_hand, hand, table_deck
        
        def check_blackjack(dealer_hand):
            total_val = 0
            card_deck_built = card_deck.CardBuilder.card_builder_dict()
            blackjack = False
            for item in dealer_hand:
                total_val += int(card_deck_built[item])
                if 21 ==  total_val:
                    print('Dealer has blackjack! Down bad.')
                    blackjack = True
                else:
                    blackjack = False
            return blackjack

