#Class for players

from card_deck import CardBuilder


class Players:
    
    import card_deck

    def get_hand():
            player_hand = []
            return player_hand

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def check_player_blackjack(hand):
        total_val = 0
        card_dict = CardBuilder.card_builder_dict()
        blackjack = False
        for item in hand:
            total_val += int(card_dict[item])
            if 21 ==  total_val:
                print('Player has blackjack! Easy money.')
                blackjack = True
            else:
                blackjack = False
        return blackjack