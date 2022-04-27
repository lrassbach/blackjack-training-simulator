#ui class

class UI:
    def welcome():
        print('Welcome to the Blackjack Trainer!')
        print('This program is designed to help you practice your blackjack.')
        print('Enter q to quit at any time.')
    
    def hand_display(dealer_hand, hand):
        print('Dealer shows:', dealer_hand[1])
        print('Your hand:', hand[0],',', hand[1])

    def get_user_action():
            valid = False
            while valid == False:
                choice = input('What would you like to do? Type "s" for stand, "h" for hit, "sp" for split, "d" for double.\nIf you would like to quit, enter q.\nChoice:')
                valid_input_list = ['s','h','sp','d','q','Q']
                if choice in valid_input_list:
                    valid = True
                else:
                    valid = False
                if valid == True:
                    return choice
                else:
                    print('Error! Invalid entry.')

    def action_check(choice, action):
            check = False
            quit = False
            quitter = ['q','Q']
            if choice == action:
                check = True
                print("Correct!")
                return check, quit
            if choice in quitter:
                quit = True
                return check, quit
            else:
                print("WRONG. The correct choice was "+str(action))
                return check, quit
    
    def another_game():
        #TODO make "valid choice" into a single callable method
        valid = False
        while valid == False:
            choice = input('Would you like to go again? Enter "Y" for yes or "N" for no:')
            valid_input_list = ['Y','y','N','n']
            if choice in valid_input_list:
                valid = True
            else:
                valid = False
            if valid == True:
                break    
            else:
                print('Error! Invalid entry.')
        yes = ['Y','y']
        no = ['N', 'n']
        if choice in yes:
            another = True
        elif choice in no:
            another = False
        else:
            print('Error in UI choice selection function')
        return another

#TODO Add a "Thanks for playing"