#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Incase needed as a .py file
get_ipython().system('jupyter nbconvert --to script blackjack_player.ipynb')


# In[1]:


#Importing classes from the file Deck
from Deck import Cards, Moves, Visualisation


# In[2]:


#Adding player to play against
def added_player():
    game = Moves()
    game.picking_a_card()
    game.counting_cards()   
    game.picking_a_card()
    game.counting_cards() 
    while game.count < 15:
        game.hit_another_player()
    return game.count


# In[3]:


#Calling player
#can add more than 1 if wanted
player1 = added_player()


# In[4]:


#Funtion to play the game
def play():
    name = input('Welcome to BlackJack! What is your name?')
    print(f'Hi {name}! Lets play!')
    #Calling classes from Deck
    game = Visualisation()
    #Picking first two cards
    game.picking_a_card()
    game.counting_cards()   
    game.picking_a_card()
    game.counting_cards() 
    print(f'Your first two cards are {game.card[2]} of {game.card[3]}s and {game.card[0]} of {game.card[1]}s') 
    print(f'You have {game.count} points so far')
    #Showing pictures of first two cards
    game.creation()
    #Next move
    move = input('Would you like to hit or stand?')
    if move == 'hit'.lower():
        game.hit()
        game.creation2()
        if game.count <= 21:
            move = input('Would you like to hit or stand?')
            if move == 'hit'.lower():
                game.hit()
                game.creation3()
                if game.count <= 21:
                    move = input('Would you like to hit or stand?')
                    if move == 'hit'.lower():
                        game.hit()
                        game.creation4()
                    elif move == 'stand'.lower():
                        game.stand()
                    else:
                        raise ValueError('Please enter hit or stand')
            elif move == 'stand'.lower():
                game.stand()
            else:
                raise ValueError('Please enter hit or stand')
    elif move == 'stand'.lower():
        game.stand()
    else:
        raise ValueError('Please enter hit or stand')
    #If statements to show who won
    #If more players are added, need to be added to if statements
    if game.count > player1 and game.count <= 21:
        print("Congratulations! You've won!")
    elif game.count == player1 and game.count <= 21:
        print("Well Done! It's a draw")
    else:
        print('Better luck next time')

#Calling function
if __name__ == '__main__':
    play()


# In[ ]:




