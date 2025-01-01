#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Deck import Cards, Moves, Visualisation


# In[11]:


def added_player():
    game = Moves()
    game.picking_a_card()
    game.counting_cards()   
    game.picking_a_card()
    game.counting_cards() 
    while game.count < 15:
        game.hit()
    return game.count


# In[12]:


player1 = added_player()


# In[14]:


def play():
    name = input('Welcome to BlackJack! What is your name?')
    print(f'Hi {name}! Lets play!')
    game = Visualisation()
    game.picking_a_card()
    game.counting_cards()   
    game.picking_a_card()
    game.counting_cards() 
    print(f'Your first two cards are {game.card[2]} of {game.card[3]}s and {game.card[0]} of {game.card[1]}s') 
    print(f'You have {game.count} points so far')
    game.creation()
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
    if game.count > player1 and game.count <= 21:
        print("Congratulations! You've won!")
    elif game.count == player1 and game.count <= 21:
        print("Well Done! It's a draw")
    else:
        print('Better luck next time')
    
if __name__ == '__main__':
    play()


# In[ ]:




