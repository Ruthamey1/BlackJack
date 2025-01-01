#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Using Jupyer notebook converts to .py so can interact across different notebooks
get_ipython().system('jupyter nbconvert --to script Deck.ipynb')


# In[1]:


#Importing neccesary library
import random
import cv2
import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame, Label, Tk
from PIL import Image, ImageTk


# In[1]:


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
            try:
                points = int(input('Would you like to choose Ace to have the value 1 or 11?'))
                self.count += points
            except ValueError:
                print('Please enter a valid number')
        else:
            self.count += self.card[0]


# In[3]:


#Moves inherites Cards
class Moves(Cards):

    def __init__(self):
        super().__init__()

    #picking a new card, counting it, seeing if you're bust
    def hit(self):
        self.picking_a_card()
        self.counting_cards() 
        if self.count > 21:
            print(f'You picked the {self.card[0]} of {self.card[1]}s')
            print("Uh oh you're bust, you've lost!")
        else:
            print(f'You picked the {self.card[0]} of {self.card[1]}s')
            print(f'You now have {self.count} points')

    #Finalising your count
    def stand(self):
        print(f'Your final count is {self.count}')


# In[4]:


#Visualising cards which have been chosen
#Function to read image of second card
from functools import partial

class Visualisation(Moves):
    
    def __init__(self):
        super().__init__()
    
    def card1(self, frame_plot):
        card1 = f'{self.card[-2]}_of_{self.card[-1]}s.png'
        test = cv2.imread(f'PNG-cards-1.3/{card1}')
        test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        #Reszing image
        test = cv2.resize(test, (200,300), interpolation=cv2.INTER_AREA)
        #Converting image to PIL format
        image = Image.fromarray(test)
        photo = ImageTk.PhotoImage(image)
        self.display_photo(photo, frame_plot)
    
    #Function to read image of second card
    def card2(self, frame_plot):
        card2 = f'{self.card[-4]}_of_{self.card[-3]}s.png'
        test = cv2.imread(f'PNG-cards-1.3/{card2}')
        test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        #Reszing image
        test = cv2.resize(test, (200,300), interpolation=cv2.INTER_AREA)
        #Converting image to PIL format
        image = Image.fromarray(test)
        photo = ImageTk.PhotoImage(image)
        self.display_photo(photo, frame_plot)

    #Function to read image of second card
    def add_card(self, frame_plot):
        card2 = f'{self.card[-6]}_of_{self.card[-5]}s.png'
        test = cv2.imread(f'PNG-cards-1.3/{card2}')
        test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        #Reszing image
        test = cv2.resize(test, (200,300), interpolation=cv2.INTER_AREA)
        #Converting image to PIL format
        image = Image.fromarray(test)
        photo = ImageTk.PhotoImage(image)
        self.display_photo(photo, frame_plot)

     #Function to read image of second card
    def add_card4(self, frame_plot):
        card2 = f'{self.card[-8]}_of_{self.card[-7]}s.png'
        test = cv2.imread(f'PNG-cards-1.3/{card2}')
        test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        #Reszing image
        test = cv2.resize(test, (200,300), interpolation=cv2.INTER_AREA)
        #Converting image to PIL format
        image = Image.fromarray(test)
        photo = ImageTk.PhotoImage(image)
        self.display_photo(photo, frame_plot)

    def add_card5(self, frame_plot):
        card2 = f'{self.card[-10]}_of_{self.card[-9]}s.png'
        test = cv2.imread(f'PNG-cards-1.3/{card2}')
        test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        #Reszing image
        test = cv2.resize(test, (200,300), interpolation=cv2.INTER_AREA)
        #Converting image to PIL format
        image = Image.fromarray(test)
        photo = ImageTk.PhotoImage(image)
        self.display_photo(photo, frame_plot)
    
    #Function to display plot in the Tkinter window
    def display_photo(self, photo, frame_plot):
        for widget in frame_plot.winfo_children():
            widget.destroy()  # Clears previous plot
        label = Label(frame_plot, image=photo)
        label.image = photo 
        label.pack()

    def first_two_buttons(self, frame_buttons, frame_plot):
        #Adding a button to see first card
        first_card = ttk.Button(frame_buttons, text="First Card", command=partial(self.card1, frame_plot))
        first_card.pack(pady=5, fill='x')
        
        #Adding a button to see second card
        second_card = ttk.Button(frame_buttons, text="Second Card", command=partial(self.card2, frame_plot))
        second_card.pack(pady=5, fill='x')

    def add_button(self, frame_buttons, frame_plot):
        #Adding a button to see first card
        next_card3 = ttk.Button(frame_buttons, text="Third Card", command=partial(self.add_card, frame_plot))
        next_card3.pack(pady=5, fill='x')

    def add_button4(self, frame_buttons, frame_plot):
        #Adding a button to see first card
        next_card4 = ttk.Button(frame_buttons, text="Fourth Card", command=partial(self.add_card4, frame_plot))
        next_card4.pack(pady=5, fill='x')

    def add_button5(self, frame_buttons, frame_plot):
        #Adding a button to see first card
        next_card5 = ttk.Button(frame_buttons, text="Fifth Card", command=partial(self.add_card5, frame_plot))
        next_card5.pack(pady=5, fill='x')
    
    
    def creation(self):
        #Creating the main Tkinter window
        root = tk.Tk()
        root.title("Blackjack")
        root.geometry("500x400")
        
        #A frame to hold the buttons on the left
        frame_buttons = ttk.Frame(root)
        frame_buttons.pack(side="left", padx=20, pady=20)
        
        #A frame to hold the plot area
        frame_plot = ttk.Frame(root)
        frame_plot.pack(side="right", padx=20, pady=20, fill="both", expand=True)
        
        self.first_two_buttons(frame_buttons, frame_plot)
        
        root.mainloop()

    def creation2(self):
        #Creating the main Tkinter window
        root = tk.Tk()
        root.title("Blackjack")
        root.geometry("500x400")
        
        #A frame to hold the buttons on the left
        frame_buttons = ttk.Frame(root)
        frame_buttons.pack(side="left", padx=20, pady=20)
        
        #A frame to hold the plot area
        frame_plot = ttk.Frame(root)
        frame_plot.pack(side="right", padx=20, pady=20, fill="both", expand=True)
        
        self.first_two_buttons(frame_buttons, frame_plot)

        self.add_button(frame_buttons, frame_plot)
        
        root.mainloop()

    def creation3(self):
        #Creating the main Tkinter window
        root = tk.Tk()
        root.title("Blackjack")
        root.geometry("500x400")
        
        #A frame to hold the buttons on the left
        frame_buttons = ttk.Frame(root)
        frame_buttons.pack(side="left", padx=20, pady=20)
        
        #A frame to hold the plot area
        frame_plot = ttk.Frame(root)
        frame_plot.pack(side="right", padx=20, pady=20, fill="both", expand=True)
        
        self.first_two_buttons(frame_buttons, frame_plot)

        self.add_button(frame_buttons, frame_plot)
        
        self.add_button4(frame_buttons, frame_plot)
        
        root.mainloop()
        
    def creation4(self):
        #Creating the main Tkinter window
        root = tk.Tk()
        root.title("Blackjack")
        root.geometry("500x400")
        
        #A frame to hold the buttons on the left
        frame_buttons = ttk.Frame(root)
        frame_buttons.pack(side="left", padx=20, pady=20)
        
        #A frame to hold the plot area
        frame_plot = ttk.Frame(root)
        frame_plot.pack(side="right", padx=20, pady=20, fill="both", expand=True)
        
        self.first_two_buttons(frame_buttons, frame_plot)

        self.add_button(frame_buttons, frame_plot)

        self.add_button4(frame_buttons, frame_plot)

        self.add_button5(frame_buttons, frame_plot)
        
        root.mainloop()


# In[5]:


# Test the class
#if __name__ == "__main__":
#   app = Visualisation()
#   app.creation()


# In[ ]:





# In[ ]:




