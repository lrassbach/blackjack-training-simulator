dictionary_test_1 = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}
dictionary_test_2 = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}
dictionary_test_3 = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}

list_test = [dictionary_test_1, dictionary_test_2, dictionary_test_3] 

import card_deck



hand = ['Ace of Spades', '2 of Hearts']

hand_value = 0
card_deck_dict = card_deck.CardBuilder.card_builder_dict()
for item in hand:
    hand_value += card_deck_dict[item]

#print(hand_value)



#empty_list = []
#empty_list.append(dictionary_test.pop("key1"))
#print(empty_list)
#print(dictionary_test)
#print(dictionary_test["key1"])

# import card_deck as cd

# card_deck_built = cd.CardBuilder.card_builder()

# #can reference the keys in the hands from basic card deck object 

# dealer_hand = ['Ace of Spades','Jack of Spades']

