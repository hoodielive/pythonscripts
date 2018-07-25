#!/usr/bin/env python3

import collections 

Card = collections.namedtuple('Card', ['rank', 'suit']) 

# this code demonstrates the power of implementing: -> special methods -> ('__getitem__'|'__len__'_) 

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
    suits = 'spades diamonds clubs hearts'.split() 

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] 
        print(type(self._cards)) 

    def __len__(self):
        return len(self._cards) 

    def __getitem__(self, position): 
        return self._cards[position] 

beer_card = Card('7', suit='diamonds')
print(beer_card) 
deck = FrenchDeck() 
print(deck[0]) 
