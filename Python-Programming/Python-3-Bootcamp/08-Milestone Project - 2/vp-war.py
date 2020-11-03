# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:15:37 2020

@author: vivek
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') # this is a tuple because we dont want to change this
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11} # this is a dictionary of key-value pairs

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank    
        self.value=values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
# deck class
# 0. deck class holds a list of card objects (i.e. deck class will return Card class object instances, not just normal python data types)
# 1. instantiate a deck of 52 class objects and hold them as a list of card objects
# 2. shuffle the deck by calling random.shuffle() function
# 3. deal cards from deck object using pop method
  
class Deck:
    def __init__(self):
        self.all_cards = []  # start with an empty list
        for suit in suits: # to instantiate the deck
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def __str__(self):
        pass
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop() # returns one card by popping it off the list

'''
# how shuffle works
a=Deck()

print(a.all_cards[-1]) # print the last card
Ace of Clubs

a.shuffle()

print(a.all_cards[-1]) # print the last card again
King of Spades
'''

'''
# how pop works
a=Deck()

my_card=a.deal_one()

print(my_card)
Ace of Clubs

len(a.all_cards)
Out[37]: 51 # notice the length of deck reduces from 52 to 51
'''

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)==type([]): #list of multiple card objects
            self.all_cards.extend(new_cards)
        else: # for a single card object
            self.all_cards.append(new_cards)        
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'

'''
c=Card('Clubs','Ace')

print(c)
Ace of Clubs

p=Player('vivek')

print(p)
player vivek has 0 cards.

p.add_cards(c)

print(p)
player vivek has 1 cards.

print(p.all_cards[0])
Ace of Clubs

p.remove_one() # removes one card from players deck
'''


# game setup

p1 = Player('One')
p2 = Player('Two')

d = Deck()
d.shuffle()

for x in range(26):
    p1.add_cards(d.deal_one())
    p2.add_cards(d.deal_one())

g_on = True

round_num=0
while g_on==True:
    # track and show the round number
    round_num += 1
    print(f'Round {round_num}')
    
    # see if either player has already won
    if len(p1.all_cards)==0: # all_cards are all cards of player 1
        print(f'{p1.name} out of cards, {p2.name} wins!')
        g_on=False
        break
    if len(p2.all_cards)==0: # all_cards are all cards of player 2
        print(f'{p2.name} out of cards, {p1.name} wins!')
        g_on=False
        break

    # start a new round
    player_one_cards = [] # current cards in play of player 1
    player_one_cards.append(p1.remove_one())    
    player_two_cards = [] # current cards in play of player 2    
    player_two_cards.append(p2.remove_one())
    
    # while at war
    # three possible scenarios - card of p1 > p2, p1 < p2 or p1 == p2
    # if cards  p1==p2, war happens and both players need to draw 5 additional cards
    # if they dont have 5 additional cards they loose
    at_war=True
    while at_war==True:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            p1.add_cards(player_one_cards)
            p1.add_cards(player_two_cards)
            at_war=False
        if player_one_cards[-1].value < player_two_cards[-1].value:
            p2.add_cards(player_one_cards)
            p2.add_cards(player_two_cards)
            at_war=False
        else:
            print('WAR!')
            if len(p1.all_cards)<3:
                print(f'{p1.name} unable to declare war, {p2.name} wins!')
                g_on=False
                break
            elif len(p2.all_cards)<3:
                print(f'{p2.name} unable to declare war, {p1.name} wins!')
                g_on=False
                break
            else:
                for num in range(3): # draw 3 cards for both players
                    player_one_cards.append(p1.remove_one())
                    player_two_cards.append(p2.remove_one())
                    
