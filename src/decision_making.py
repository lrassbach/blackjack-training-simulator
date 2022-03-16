###Decision Making Class

import card_deck

class PlayerChoice:
    #this function determines the value of the players hand

    def get_user_action():
        valid = False
        while valid == False:
            choice = input('What would you like to do? Type "s" for stand, "h" for hit, "sp" for split, "d" for double:')
            valid_input_list = ['s','h','sp','d']
            if choice in valid_input_list:
                valid = True
            else:
                valid = False
            if valid == True:
                return choice
                break    
            else:
                print('Error! Invalid entry.')
        #TODO need to add a validation check for the input; use while loop that has a boolean that is 'valid' and allow to run while boolean is TRUE
        #TODO move this function to UI

    
#TODO move methods in this class to player class


choice = PlayerChoice.get_user_action()       
print('player chose', choice)            
