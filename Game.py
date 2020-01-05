'''
one of the 2 files that form the BlackJack Game
(C) Justin Varela, 2019, Lisbon, Portugal
this file contains the loops and the functions that 
make the actual game
it's importing from the Classes file
'''
import Classes
import time

while True:
    '''
    this loop happens once a game
    this simulates the player sitting at the table
    '''
    print("Welcome to Casino Estoril. My name is Joaquim and")
    print("I'll be your dealer tonight")

    starting_balance = 0
    counter = 0
    new_hand = True

    while starting_balance == 0 or starting_balance % 5 != 0:
        '''
        also, this loop only happens once
        creates the client's balance for the entire game
        '''
        if counter == 0:
            try:
                starting_balance = int(input("So, With how much do you want play with?"))
            except:
                print("Sorry? How much? It must be a number.")
            finally:
                counter += 1
        else:
            try:
                starting_balance = int(input("Only multiples of 5, Sir."))
            except:
                print("Sorry? How much? It must be a number.")
            else:
                print("Thank You")

    bank = Classes.Chips(starting_balance)
    while new_hand:
        '''
        a loop for each play or hand
        creates a deck, shuffles it
        '''
        blackjack = False
        Classes.player_turn = True
        game_deck = Classes.Deck()
        game_deck.shuffle()

        Classes.take_bet(bank) # takes the players bet
        time.sleep(2)
        print("Burned card...")
        game_deck.burn_card()

        phand = Classes.Hand()
        dhand = Classes.Hand()

        Classes.dealing(game_deck,phand,dhand)

        # from here to the line 87, is the player's BJ scenario
        if phand.value == 21:
            blackjack = True
            print("BlackJack!")
        
            if Classes.values[dhand.cards[0].rank] == 10:
                print("\nLet's see what I have")

            elif dhand.cards[0].rank == 'Ace':
                bj_agains_ace = input("Do you wish to receive the prize now or try the BlackJack price?")
                
                while bj_agains_ace != 'y' or bj_agains_ace != 'n':
                    
                    if bj_agains_ace.lower() == 'y':
                        Classes.player_wins(bank)
                    
                    elif bj_agains_ace.lower() == 'n':
                        print("OK")
                    
                    else:
                        print("Sorry?...")
            
            else:
                print("You win!")
                Classes.player_BJ(bank)

        else:

            while Classes.player_turn:
                print("You have", phand.value)
                time.sleep(2)
                Classes.hit_or_stand(game_deck,phand)
                time.sleep(3)
                if phand.value > 21:
                    Classes.player_bust(bank)
                    Classes.player_turn = False
        
        # from here to line 114, is the dealer's turn
        # he keeps drawing cards until he has 17 or more
        # only happens if the player doesn't have BJ or busts
        if phand.value <= 21:

            Classes.show_all_cards(phand,dhand)
            time.sleep(2)

            while dhand.value < 17:
 
                Classes.hit(game_deck,dhand)
                print(dhand)
                time.sleep(5)
            
                Classes.show_all_cards(phand,dhand)
                time.sleep(3)

            # from here to line 128, is the end of game scenarios
            # also the comparing hands section
            if dhand.value > 21:
                Classes.dealer_bust(bank)
            elif dhand.value > phand.value:
                Classes.dealer_wins(bank)
            elif dhand.value < phand.value and blackjack:
                Classes.player_BJ(bank)
            elif dhand.value < phand.value:
                Classes.player_wins(bank)
            else:
                Classes.push_tie()
        
        # after the play is over, we tell the player his balance
        print("Your balance: ",bank.balance)
        time.sleep(3)

        # if the player's balance is lower than 5 (a chip is worth 5)
        # the player doesn't get to play anymore (no buybacks in a dream world)
        if bank.balance < 5:
            print("That's enough for tonight, Sir. Have a pleasant evening")
            break
        else: # here we ask the player if he wants to play another hand
            newgame = input("Do you want to play again? ('y' or 'n'?")

        if newgame.lower() == 'y':
            new_hand = True
            continue
        else:
            print("Thanks You very much Sir. Have a pleasant evening")
            break





        
    





















