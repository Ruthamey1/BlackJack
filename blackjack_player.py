#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Deck import Cards, Moves


# In[11]:


get_ipython().system('jupyter nbconvert --to script blackjack_player.ipynb')


# In[12]:


get_ipython().system('pwd')


# In[3]:


def play():
    name = input('Welcome to BlackJack! What is your name?')
    print(f'Hi {name}! Lets play!')
    game = Cards()
    game.picking_a_card()
    game.counting_cards()   
    game.picking_a_card()
    game.counting_cards() 
    print(f'Your first two cards are {game.card[0]} of {game.card[1]}s and {game.card[2]} of {game.card[3]}s') 
    print(f'You have {game.count} points so far')
    move = Moves()
    move.next_move()
    print(f'You picked the {game.card[0]} of {game.card[1]}s')
if __name__ == '__main__':
    play()


# In[ ]:




