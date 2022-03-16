#This class encompasses evaluating the players hand vs the dealers hand & choices made to determine outcome 

#TODO: should this class be added to hand evaluation? I'm thinking yes but im not sure

from card_deck import CardBuilder


class SoftTotals:
    # this method determines soft totals 
    #TODO need to update to include if soft totals is double aces   
    def soft_check(hand):
        x = 0
        soft_tag = 0
        #determine if an ace has been dealt to this hand
        ace_spot = []
        for item in hand:
            a = item[0:3]
            if a == 'Ace':
                ace_spot.append(x)
            x += 1
        card_deck_built = CardBuilder.card_builder()
        #identify if the ace results in a hard or soft total
        x = 0
        for item in hand:
            x += card_deck_built[item]
        if x < 17 or  x == 22:
            soft_tag = 1
        #return the location of the ace if there is one, and identifies the hand as soft or not
        return soft_tag, ace_spot
    
    def use_soft_check(hand, soft_tag):
        #TODO finish this method and review if needed in this version
        use_soft_deck = 0
        x = 0
        card_deck_built = CardBuilder.card_builder()
        for item in hand:
            x += card_deck_built[item]
        if x > 17 and sum != 22:
            use_soft_deck == 1

    def assign_soft_values(hand, soft_tag, ace_spot):
        #TODO need to finish this method or figure out if its needed
        if soft_tag == 1 and int(len(ace_spot)) >= 1:
            card_deck_built = CardBuilder.soft_card_builder()
            return card_deck_built
        else:
            card_deck_built = CardBuilder.card_builder()
        return card_deck_built


        

hand = ['4 of Spades', 'Ace of Spades']
soft_tag, ace_spot = SoftTotals.soft_check(hand)
card_deck_built = SoftTotals.assign_soft_values(hand, soft_tag, ace_spot)

print(soft_tag)
print(ace_spot)

# print(card_deck_built[hand[0]])
# print(len(ace_spot))