from tkinter import * 
import random, variabelen
from PIL import Image, ImageTk
from tkinter import messagebox

def roulette():
    window = Tk()
    window.title("Deck met kaarten")
    window.geometry("1300x900")
    window.configure(background= "#5d0303")
    score = 0

    def balletje_gok(gok):
        pass


    #hoofdframe voor het spel
    main_frame = Frame(window, bg= "#5d0303")
    main_frame.pack()

    #frame voor het roterende balletje?
    bal_frame = LabelFrame(main_frame, bg="#efa70c")
    bal_frame.grid(row= 0, column= 0, padx=20, pady=20)

    #frame voor het plaatsen van je gok
    gok_frame = LabelFrame(main_frame, bg="#efa70c")
    bal_frame.grid(row= 0, column= 1, padx=20, pady=20)

    #knoppen voor het gokken pos 1-15, groen en kleur(zwart/rood)
    knop1 = Button(gok_frame, text="Hit", font=("Helvetica", 14),bg="#5d0303", fg="#efa70c", activebackground="#840707", activeforeground="#a27108")
    knop1.grid()
    knop2 = Button(gok_frame,)
    knop2.grid()
    knop3 = Button(gok_frame,)
    knop3.grid()
    knop4 = Button(gok_frame,)
    knop4.grid()
    knop5 = Button(gok_frame,)
    knop5.grid()
    knop6 = Button(gok_frame,)
    knop6.grid()
    knop7 = Button(gok_frame,)
    knop7.grid()
    knop8 = Button(gok_frame,)
    knop8.grid()
    knop9 = Button(gok_frame,)
    knop9.grid()
    knop10 = Button(gok_frame,)
    knop10.grid()
    knop11 = Button(gok_frame,)
    knop11.grid()
    knop12 = Button(gok_frame,)
    knop12.grid()
    knop13 = Button(gok_frame,)
    knop13.grid()
    knop14 = Button(gok_frame,)
    knop14.grid()
    knop15 = Button(gok_frame,)
    knop15.grid()
    knop16_groen = Button(gok_frame,)
    knop16_groen.grid()
    knop17_zwart = Button(gok_frame,)
    knop17_zwart.grid()
    knop18_rood = Button(gok_frame,)
    knop18_rood.grid()

    window.mainloop()

roulette()