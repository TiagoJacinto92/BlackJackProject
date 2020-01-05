'''
one of the 2 files that form the BlackJack Game
(C) Justin Varela, 2019, Lisbon, Portugal
this file contains the Classes, Global Variables and Functions that 
are used in the game
'''


import random # used to shuffle the deck
import time # puts time in between game sequences, such as drawing cards

# global variables suits, ranks and values are used to create the cards later
suits = ('Hearts', 'Spades','Diamonds','Clubs')
ranks = ('Two','Three','Four', 'Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King',
'Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
'Jack':10,'Queen':10,'King':10,'Ace':11}

player_turn = True # a global variable used to break out of a while loop later

class Card:
    '''
    Each card has a suit and a rank, these originating from the globals above
    The print method prints a card, e.g. "Two of Hearts"
    '''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    '''
    Holds the 52 cards objects in a list that can be shuffled
    The init method instantiates all 52 cards using the Card class
    2 for loops, 1 for each list, suits and ranks
    this way, we can put the suits and ranks together
    '''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__() # or str(card)
        return 'The deck has:' + deck_comp
    
    def shuffle(self):
        '''
        shuffles the deck
        '''
        random.shuffle(self.deck)
        
    def burn_card(self):
        '''
        burns a card, just like in blackjack
        '''
        self.deck.pop()
    
    def __len__(self):
        '''
        just to troubleshoot some problem in construction
        '''
        return len(self.deck)
        
    def deal(self):
        '''
        takes a card from the top of the deck
        retains that card's value
        '''
        one_card = self.deck.pop()
        return one_card
    
class Hand:
    '''
    2 Hand objects, the player's and the dealer's
    this class calculates the value of each hand
    additionally, adjusts the value to the aces
    '''
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        '''
        adds a card from the deck.deal method
        '''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 # counts the aces for the later method
            
    def __str__(self):
        cards_list = ''
        for card in self.cards:
            cards_list += '\n' + str(card)
        return cards_list
    
    def __len__(self):
        '''
        troubleshoot
        '''
        cards_list = ''
        for card in self.cards:
            cards_list += '\n' + str(card)
        return len(cards_list)
    
    def adjust_for_ace(self):
        '''
        takes 10 of the value if the hand's is above 21
        '''
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    '''
    this class keeps track of the player's chips
    also, his winnings and losses after each play
    '''
    def __init__(self,balance):
        self.balance = balance
        self.bet = 0
        
    def __str__(self):
        
        if self.balance / 5 > 1 or self.balance / 5 == 0:
            return f'Balance: {self.balance}€, that makes {int(self.balance / 5)} chips'
        else:
            return f'Balance: {self.balance}€, that makes {int(self.balance / 5)} chip'
            
    def win_bet(self):
        self.balance += self.bet

    def win_bet_BJ(self):
        self.balance += self.bet + (self.bet / 2) # different winnings if the player has BJ
        
    def lose_bet(self):
        self.balance -= self.bet


def take_bet(balance):
    '''
    asks the player for the play's bet
    '''
    while True:
        try:
            balance.bet = int(input("Bet..."))
            while True:
                if balance.bet > balance.balance:
                    print("No sufficient funds...")
                    balance.bet = int(input("Bet..."))
                else:
                    print("Thank You")
                    break
            break
        except ValueError:
            print("That's not a value. Please, give a valid bet")

def hit(deck,hand):
    '''
    takes a card from the deck object and adds it to the hand one
    '''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    print(hand.cards[-1])

def hit_or_stand(deck,hand):
    '''
    using a while loop to ask the player to choose his next move
    the global variable controls the loop
    '''
    global player_turn
    
    while True:

        x = input("Your move Sir. Hit or Stand?('H' or 'S')")
        if x.lower() == 'h':
            hit(deck,hand)
        elif x.lower() == 's':
            print("My turn")
            player_turn = False
        else:
            print("Sorry, Sir. Please try again")
            continue
        break

def dealing(deck,hand1,hand2):
    '''
    transfers code from the game file to this file
    this part calls the necessary functions to begin the game
    add_card, deal and adjust_for_ace
    '''
    hand1.add_card(deck.deal())
    print(str(hand1))
    time.sleep(3)
    
    hand1.add_card(deck.deal())
    print("You have: ",str(hand1))
    time.sleep(5)
        
    hand2.add_card(deck.deal())

    hand2.add_card(deck.deal())
    print("I have: "+ str(hand2.cards[0]) + " showing")
    time.sleep(3)

    hand1.adjust_for_ace()
    hand2.adjust_for_ace()

def show_cards(hand1,hand2):
    '''
    shows the player's cards and only one of the dealer's cards
    '''
    print("You have: ",str(hand1),hand1.value)
    print("I have: ",hand2.cards[0])

def show_all_cards(hand1,hand2):
    '''
    later on, the dealer will show his second card
    '''
    print("You have: ",str(hand1),"\n",hand1.value)
    print("I have: ",str(hand2),"\n",hand2.value)

# the functions below are the end of game scenarios
    
def dealer_bust(chips):
    '''
    dealer busts and loses
    player wins the bet, adding the winnings to his chips
    '''
    print("Dealer Bust!")
    print("You win!")
    chips.win_bet()

def player_wins(chips):
    '''
    player's hand's value is higher than the dealer's
    player wins the bet, adding the winnings to his chips
    '''
    print("You win!")
    chips.win_bet()

def player_bust(chips):
    '''
    player busts
    player loses the bet, deducting the losses from his chips
    '''
    print("Bust!")
    print("You lose!")
    chips.lose_bet()

def dealer_wins(chips):
    '''
    player's hand's value is lower than the dealer's
    player loses the bet, deducting the losses from his chips
    '''
    print("Dealer wins")
    chips.lose_bet()

def player_BJ(chips):
    '''
    player's wins with BJ against no BJ from the dealer
    player wins the bet, adding the BJ winnings to his chips
    '''
    chips.win_bet_BJ()

def push_tie():
    '''
    there's a tie
    player keeps his bet
    '''
    print("It's a push!")

        

    
