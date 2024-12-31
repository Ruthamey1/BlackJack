#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


class Cards:
    def __init__(self):
        self.count = 0
        self.card = []

    #Function to generate card and stop from being picked twice
    def random_generator(self):
        random_card = random.randint(1,52)
        if random_card in card:
            random_generator()
        else:
            return random_card

    def picking_a_card(self, random_card):
        if random_card in range(1,14):
            sorting_cards('club', random_card)
        elif random_card in range(14,27):
            random_card = random_card-13
            sorting_cards('diamond', random_card)
        elif random_card in range(27,40):
            random_card = random_card-26
            sorting_cards('spade', random_card)
        elif random_card in range(40,53):
            random_card = random_card-38
            sorting_cards('heart', random_card)
        
    def sorting_cards(self, suit, random_card):
        if random_card in range(2,11):
            card.insert(0, suit)
            card.insert(0, random_card)
        elif random_card == 1:
            card.insert(0, suit)
            card.insert(0, 'ace')
        elif random_card == 11:
            card.insert(0, suit)
            card.insert(0, 'jack')
        elif random_card == 12:
            card.insert(0, suit)
            card.insert(0, 'queen')
        elif random_card == 13:
            card.insert(0, suit)
            card.insert(0, 'king')

    def counting_cards(self, card):
        global count
        if card == 'jack' or card == 'queen' or card == 'king':
            count += 10
        elif card == 'ace':
            points = int(input('Would you like to choose Ace to have the value 1 or 11?'))
            count += points
        else:
            count += card


# In[ ]:




