
####Card Deck
####Builds a Card Deck based on the parameters you choose

def card_builder():
    #input number of suits & determine length
    num_suits = 4
    ##input("How many suits would you like in this card deck?:") Needs to be added back in for completed product
    num_suits = int(num_suits)
    deck_length = (52 / 4) * num_suits
    deck_length = int(deck_length)
    #print(num_suits,"suits;",deck_length,"cards")
    #takes inputs and determines number of suits
    suit_list = ["Hearts","Clubs","Spades","Diamonds"]
    suits_reqd = []
    x = 0
    for item in num_suits:
        suits_reqd.insert(x,suit_list[x])
    #print(suits_reqd)
    #uses length and number of suits to create a dictionary
    card_deck = {
        }
    positional_list_card_deck = []
    x = 0
    y = 0
    face = ["Jack","Queen","King","Ace"]
    def dict_card_build(x,y):    
        for item in range(deck_length):
            if x <= 9:
                card = str(x+1) + " of " + str(suits_reqd[y])
                card_deck[card] = x + 1
                positional_list_card_deck.append(card)
                x = x + 1
            elif 9 < x <= 12:
                card = str(face[x-10]) + " of " + str(suits_reqd[y])
                card_deck[card] = 10
                positional_list_card_deck.append(card)
                x = x + 1
            elif x == 13:
                card = str(face[x-10]) + " of " + str(suits_reqd[y])
                card_deck[card] = 11
                positional_list_card_deck.append(card)
                x = x + 1
    for item in suits_reqd:
        dict_card_build(x,y)
        y = y + 1
    #print(positional_list_card_deck)
    return card_deck,positional_list_card_deck

card_deck_built,positional_list_card_deck = card_builder()            

###This unit creates a table environment
###with all the functions of a blackjack table

#table

import random

def table_environment(card_deck,positional_list_card_deck):
    deck = card_deck
    #this function puts together the table deck
    def table_deck_builder():
        num_decks = 6
        ##input("How many decks would you like for blackjack? (6 is standard in most casinos):")
        table_deck = []
        x = 0
        for item in range(num_decks):
            table_deck.append(card_deck)
            x = x + 1
            if x == num_decks:
                break
        return table_deck
    table_deck = table_deck_builder()
    #print(len(table_deck))
    def deal_card(table_deck):
        #print(table_deck)
        dealer_hand = []
        player_hand = []
        spot_deck = []
        spot_card = []
        spot_deck_record = []
        spot_card_record = []
        ##use these records to delete from deck
        for i in range(4):
            rand_deck_spot = random.randint(0,3)
            spot_deck.append(rand_deck_spot)
            spot_deck_record.append(rand_deck_spot)
            rand_key_spot = random.randint(0,len(card_deck)-1)
            spot_card.append(rand_key_spot)
            spot_card_record.append(rand_key_spot)
        x = 0
        print(spot_deck)
        print(spot_card)
        for item in range(4):
            a = spot_deck[x]
            b = spot_card[x]
            if x % 2 == 0:
                bb = str(positional_list_card_deck[b])
                #print(bb)
                player_hand.append(table_deck[a][bb])
            else:
                bb = str(positional_list_card_deck[b])
                #print(bb)
                dealer_hand.append(table_deck[a][bb])
            x = x + 1
        return dealer_hand,player_hand
    dealer_hand,player_hand = deal_card(table_deck)
    #print("****************")
    print(dealer_hand)
    print(player_hand)
            
            
    
for item in range(100):
    table_environment(card_deck_built,positional_list_card_deck)

























