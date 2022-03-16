###Main

import card_deck as cd
import deck_positional_list as dp
import dealer
import players

card_deck_dictionary = cd.CardBuilder.card_builder_dict()

card_deck_list = cd.CardBuilder.card_builder_list()

print('break')

positional_list_card_deck = dp.deck_positional_list(4)
print('Welcome to the Blackjack Trainer!')
deck_size = 6
#input('Please enter the number of card decks you would like to use:')
table_deck = dealer.Dealer.table_deck_builder(card_deck_dictionary, deck_size)
print(len(table_deck))

dealer_hand, hand, table_deck= dealer.Dealer.deal_card(table_deck, 1)
print('Dealer shows:', dealer_hand[1])
print('Your hand:', hand[0],',', hand[1])

dealer.Dealer.check_blackjack(dealer_hand)



#method called for determining soft totals

#decision method called to interpret what the player should do

#method called for player to make an action