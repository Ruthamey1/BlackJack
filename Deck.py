#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Using Jupyer notebook converts to .py so can interact across different notebooks
get_ipython().system('jupyter nbconvert --to script Deck.ipynb')


# In[2]:


#Importing neccesary library
import random


# In[3]:


class Cards:
    #Initializing parameters
    def __init__(self):
        self.count = 0
        self.card = []
        self.used = []

    #Function to generate card and stop from being picked twice
    def random_generator(self):
        random_card = random.randint(1,52)
        if random_card in self.used:
            return self.random_generator()
        else:
            return random_card

    #Sorting integer cards from honor cards
    def sorting_cards(self, suit, random_card):
        if random_card in range(2,11):
            self.card.insert(0, suit)
            self.card.insert(0, random_card)
        elif random_card == 1:
            self.card.insert(0, suit)
            self.card.insert(0, 'ace')
        elif random_card == 11:
            self.card.insert(0, suit)
            self.card.insert(0, 'jack')
        elif random_card == 12:
            self.card.insert(0, suit)
            self.card.insert(0, 'queen')
        elif random_card == 13:
            self.card.insert(0, suit)
            self.card.insert(0, 'king')

    #Picking a card and sorting into suits
    def picking_a_card(self):
        random_card = self.random_generator()
        self.used.append(random_card)
        if random_card in range(1,14):
            self.sorting_cards('club', random_card)
        elif random_card in range(14,27):
            self.sorting_cards('diamond', random_card-13)
        elif random_card in range(27,40):
            self.sorting_cards('spade', random_card-26)
        elif random_card in range(40,53):
            self.sorting_cards('heart', random_card-39)

    #Counting value of cards given
    def counting_cards(self):
        if self.card[0] == 'jack' or self.card[0] == 'queen' or self.card[0] == 'king':
            self.count += 10
        elif self.card[0] == 'ace':
            points = int(input('Would you like to choose Ace to have the value 1 or 11?'))
            self.count += points
        else:
            self.count += self.card[0]


# In[6]:


class Moves(Cards):

    
    def __init__(self):
        super().__init__()

    def hit(self):
        self.picking_a_card()
        self.counting_cards() 
        if self.count > 21:
            print("Uh oh you're bust, you've lost!")
        else:
            print(f'You picked the {self.card[0]} of {self.card[1]}s')
            print(f'You now have {self.count} points')

    def stand(self):
        print(f'Your final count is {self.count}')

    def next_move(self):
        while self.count < 21:
            move = input('Would you like to hit or stand?')
            if move == 'hit':
                self.hit()
            elif move == 'stand':
                self.stand()
                break


# In[ ]:




