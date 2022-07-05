# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:47:37 2022

@author: Dell
"""

from tkinter import*
import random
root = Tk()
root.title("colour dictionary")
root.geometry("600x600")
root.configure(background="red")

my_dictionary = {
    "green" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]
               }

def click_me():
    random_no = random.randint(0,7)
    random_colour = my_dictionary["green"][random_no]
    print(random_colour)
    root.configure(background = random_colour)
    


btn = Button(root , text = "click me" , command = click_me)
btn.place(relx = 0.5  , rely = 0.5 , anchor  = CENTER)

root.mainloop()