from tkinter import * 
import random
from PIL import Image, ImageTk
from tkinter import messagebox

#main window voor tkinter
window = Tk()
window.title("Deck met kaarten")
window.geometry("1300x900")
window.configure(background= "#5d0303")

def stand():
    global speler_totaal, dealer_totaal, speler_score
    #totale waarde
    speler_totaal = 0
    dealer_totaal = 0

    #voeg waarde kaarten samen om tot score te komen
    for score in dealer_score:
        dealer_totaal += score

        #voeg waarde kaarten samen om tot score te komen
    for score in speler_score:
        speler_totaal += score

    hit_knop.config(state="disabled")
    stand_knop.config(state="disabled")

    #kijken of dealer moet hitten of niet
    if dealer_totaal >= 16:
        #bust?
        if dealer_totaal > 21:
            messagebox.showinfo("Speler wint", f"{dealer_totaal} Dealer bust! Speler wint!")
        #push?
        elif dealer_totaal == speler_totaal:
            messagebox.showinfo("Push!", f"{dealer_totaal} Push! Gelijkspel!")
        #Dealer win?
        elif dealer_totaal > speler_totaal:
            messagebox.showinfo("Dealer wint", f"{dealer_totaal} Dealer wint! Speler: {speler_totaal}")
        #speler win?
        else:
            messagebox.showinfo("Speler wint", f"{dealer_totaal} Speler wint! Dealer: {dealer_totaal}")
    else:
        dealer_hit()
        stand()

#blackjack na shuffle?
def shuffle_blackjack(speler):

    global speler_totaal, dealer_totaal, speler_score
    #totale waarde
    speler_totaal = 0
    dealer_totaal = 0

    if speler == "dealer":
        if len(dealer_score) == 2:
            if dealer_score[0] + dealer_score[1] == 21:
                #blackjack status veranderen
                blackjack_status["dealer"] = "ja"


    if speler == "speler":
        if len(speler_score) == 2:
             if speler_score[0] + speler_score[1] == 21:
                #blackjack status veranderen
                blackjack_status["speler"] = "ja"
        else:
            #voeg waarde kaarten samen om tot score te komen
            for score in speler_score:
                speler_totaal += score

            if speler_totaal == 21:
                blackjack_status["speler"] = "ja"
                
            elif speler_totaal > 21:
                # kijken of een aas van 11 naar 1 kan 
                for kaart_getal, kaart in enumerate(speler_score):
                    if kaart == 11:
                        speler_score[kaart_getal] = 1

                        #herberekening speler totaal
                        speler_totaal = 0
                        for score in speler_score:
                            speler_totaal += score

                        #check of totale score > 21   
                        if speler_totaal > 21:
                            blackjack_status["speler"] = "bust"
                else:
                    if speler_totaal == 21:
                        blackjack_status["speler"] = "ja"
                    if speler_totaal > 21:
                        blackjack_status["speler"] = "bust"

    

    if len(dealer_score) == 2 and len(speler_score) == 2:
        #Gelijkspel?
        if blackjack_status["dealer"] == "ja" and blackjack_status["speler"] == "ja":
            messagebox.showinfo("Push", "Het is gelijkspel!")
            hit_knop.config(state="disabled")
            stand_knop.config(state="disabled")
        #Dealer winst?
        elif blackjack_status["dealer"] == "ja":
                messagebox.showinfo("Dealer wint!", "Blackjack! Dealer wint!")
                #spel stop zetten
                hit_knop.config(state="disabled")
                stand_knop.config(state="disabled")
        #Speler winst?
        elif blackjack_status["speler"] == "ja":
                messagebox.showinfo("speler wint!", "Blackjack! speler wint!")
                #spel stop zetten
                hit_knop.config(state="disabled")
                stand_knop.config(state="disabled")
    #check voor 21 in het spel
    else:
        #Gelijkspel?
        if blackjack_status["dealer"] == "ja" and blackjack_status["speler"] == "ja":
            messagebox.showinfo("Push", "Het is gelijkspel!")
            hit_knop.config(state="disabled")
            stand_knop.config(state="disabled")
        #Dealer winst?
        elif blackjack_status["dealer"] == "ja":
                messagebox.showinfo("Dealer wint!", "21! Dealer wint!")
                #spel stop zetten
                hit_knop.config(state="disabled")
                stand_knop.config(state="disabled")
        #Speler winst?
        elif blackjack_status["speler"] == "ja":
                messagebox.showinfo("speler wint!", "21! speler wint!")
                #spel stop zetten
                hit_knop.config(state="disabled")
                stand_knop.config(state="disabled")        

    if blackjack_status["speler"] == "bust":
        messagebox.showinfo("Dealer wint!", f"{speler_totaal} Speler bust! Dealer wint!")
        #spel stop zetten
        hit_knop.config(state="disabled")
        stand_knop.config(state="disabled")

#kaart format aanpassen 
def kaart_format_fix(kaart):
    kaart_jpg = Image.open(kaart)

    kaart_jpg_format_fix = kaart_jpg.resize((240,300))

    global kaart_jpeg
    kaart_jpeg = ImageTk.PhotoImage(kaart_jpg_format_fix)

    return kaart_jpeg
    

#shuffle de kaarten
def shuffle():
    #winaar?
    global blackjack_status, speler_totaal, dealer_totaal
    #totale waarde
    speler_totaal = 0
    dealer_totaal = 0

    blackjack_status = {"dealer":"nee", "speler":"nee"}

    #spel aan zetten
    hit_knop.config(state="normal")
    stand_knop.config(state="normal")
    
    #per potje de kaarten resetten
    dealer_label_1.config(image="")
    dealer_label_2.config(image="")
    dealer_label_3.config(image="")
    dealer_label_4.config(image="")
    dealer_label_5.config(image="")

    speler_label_1.config(image="")
    speler_label_2.config(image="")
    speler_label_3.config(image="")
    speler_label_4.config(image="")
    speler_label_5.config(image="")

    #deck kaarten maken
    kaart_soorten = ["harten", "klaveren", "schoppen", "ruiten"]
    kaart_waardes = range(2, 15)

    global deck
    deck=[]
    
    for kaart_soort in kaart_soorten:
        for kaart_waarde in kaart_waardes:
            deck.append(f"{kaart_soort}_{kaart_waarde}") 

    #spelers maken
    global dealer, speler, dealer_positie, speler_positie, dealer_score, speler_score
    dealer = []
    speler = []

    dealer_score = []
    speler_score = []

    dealer_positie = 0
    speler_positie = 0
    
    #Twee kaarten voor dealer, speler shuffelen voor het begin van het spel 
    speler_hit()
    speler_hit()

    dealer_hit()
    dealer_hit()

    #Titel van de window geeft aan hoeveel kaarten al in het spel gebruikt zijn
    window.title(f"Nog {len(deck)} kaarten over")

def dealer_hit():
    global dealer_positie

    if dealer_positie < 5:
        try:
            #dealer kaarten defineren
            dealer_kaart = random.choice(deck)
            #kaart wordt uit het deck gehaald
            deck.remove(dealer_kaart)
            #dealer krijgt de kaart
            dealer.append(dealer_kaart)
            #waarde/score van kaarten dealer worden in lijst gezet
            dkaart =int(dealer_kaart.split("_", 1)[1])
            if dkaart == 14:
                dealer_score.append(11)
            elif dkaart == 11 or dkaart == 12 or dkaart == 13:
                dealer_score.append(10)
            else:
                dealer_score.append(dkaart)


            global dealer_kaart_jpg_1, dealer_kaart_jpg_2, dealer_kaart_jpg_3, dealer_kaart_jpg_4, dealer_kaart_jpg_5

            if dealer_positie == 0:
                dealer_kaart_jpg_1 = kaart_format_fix(f"kaarten/{dealer_kaart}.png")
                dealer_label_1.config(image= dealer_kaart_jpg_1)
                #aangeven dat volgende kaart gespeeld moet worden
                dealer_positie += 1

            elif dealer_positie == 1:
                dealer_kaart_jpg_2 = kaart_format_fix(f"kaarten/{dealer_kaart}.png")
                dealer_label_2.config(image= dealer_kaart_jpg_2)
                #aangeven dat volgende kaart gespeeld moet worden
                dealer_positie += 1
            
            elif dealer_positie == 2:
                dealer_kaart_jpg_3 = kaart_format_fix(f"kaarten/{dealer_kaart}.png")
                dealer_label_3.config(image= dealer_kaart_jpg_3)
                #aangeven dat volgende kaart gespeeld moet worden
                dealer_positie += 1
            
            elif dealer_positie == 3:
                dealer_kaart_jpg_4 = kaart_format_fix(f"kaarten/{dealer_kaart}.png")
                dealer_label_4.config(image= dealer_kaart_jpg_4)
                #aangeven dat volgende kaart gespeeld moet worden
                dealer_positie += 1

            elif dealer_positie == 4:
                dealer_kaart_jpg_5 = kaart_format_fix(f"kaarten/{dealer_kaart}.png")
                dealer_label_5.config(image= dealer_kaart_jpg_5)
                #aangeven dat volgende kaart gespeeld moet worden
                dealer_positie += 1

            window.title(f"Nog {len(deck)} kaarten over")

        except:
            window.title("Helaas! geen kaarten meer in het deck")

        #blackjack checken
        shuffle_blackjack("dealer")

def speler_hit():
    global speler_positie

    if speler_positie < 5:
        try:
            #speler kaarten defineren
            speler_kaart = random.choice(deck)
            #kaart wordt uit het deck gehaald
            deck.remove(speler_kaart)
            #speler krijgt de kaart
            speler.append(speler_kaart)
            #score/waarde van kaarten speler worden in lijst gezet
            skaart =int(speler_kaart.split("_", 1)[1])
            if skaart == 14:
                speler_score.append(11)
            elif skaart == 11 or skaart == 12 or skaart == 13:
                speler_score.append(10)
            else:
                speler_score.append(skaart)

            global speler_kaart_jpg_1, speler_kaart_jpg_2, speler_kaart_jpg_3, speler_kaart_jpg_4, speler_kaart_jpg_5

            if speler_positie == 0:
                speler_kaart_jpg_1 = kaart_format_fix(f"kaarten/{speler_kaart}.png")
                speler_label_1.config(image= speler_kaart_jpg_1)
                #aangeven dat volgende kaart gespeeld moet worden
                speler_positie += 1

            elif speler_positie == 1:
                speler_kaart_jpg_2 = kaart_format_fix(f"kaarten/{speler_kaart}.png")
                speler_label_2.config(image= speler_kaart_jpg_2)
                #aangeven dat volgende kaart gespeeld moet worden
                speler_positie += 1
            
            elif speler_positie == 2:
                speler_kaart_jpg_3 = kaart_format_fix(f"kaarten/{speler_kaart}.png")
                speler_label_3.config(image= speler_kaart_jpg_3)
                #aangeven dat volgende kaart gespeeld moet worden
                speler_positie += 1
            
            elif speler_positie == 3:
                speler_kaart_jpg_4 = kaart_format_fix(f"kaarten/{speler_kaart}.png")
                speler_label_4.config(image= speler_kaart_jpg_4)
                #aangeven dat volgende kaart gespeeld moet worden
                speler_positie += 1

            elif speler_positie == 4:
                speler_kaart_jpg_5 = kaart_format_fix(f"kaarten/{speler_kaart}.png")
                speler_label_5.config(image= speler_kaart_jpg_5)
                #aangeven dat volgende kaart gespeeld moet worden
                speler_positie += 1

            window.title(f"Nog {len(deck)} kaarten over")

        except:
            window.title("Helaas! geen kaarten meer in het deck")

        #blackjack checken
        shuffle_blackjack("speler")

#main frame voor tkinter
main_frame = Frame(window, bg= "#5d0303")
main_frame.pack(pady=20)

#frames voor de kaarten:
dealer_frame = LabelFrame(main_frame, text="Dealer", bd= 0, bg="#efa70c")
dealer_frame.pack(pady=10)

speler_frame = LabelFrame(main_frame, text="speler", bd= 0, bg="#efa70c")
speler_frame.pack(pady=10)

#kaarten in de frames dealer
dealer_label_1 = Label(dealer_frame, text="", bg="#efa70c")
dealer_label_1.grid(row=0, column=0, pady= 20, padx=20)

dealer_label_2 = Label(dealer_frame, text="", bg="#efa70c")
dealer_label_2.grid(row=0, column=2, pady= 20, padx=20)

dealer_label_3 = Label(dealer_frame, text="", bg="#efa70c")
dealer_label_3.grid(row=0, column=3, pady= 20, padx=20)

dealer_label_4 = Label(dealer_frame, text="", bg="#efa70c")
dealer_label_4.grid(row=0, column=4, pady= 20, padx=20)

dealer_label_5 = Label(dealer_frame, text="", bg="#efa70c")
dealer_label_5.grid(row=0, column=5, pady= 20, padx=20)

#kaarten in de frames speler
speler_label_1 = Label(speler_frame, text="", bg="#efa70c")
speler_label_1.grid(row=0, column=0, pady= 20, padx=20)

speler_label_2 = Label(speler_frame, text="", bg="#efa70c")
speler_label_2.grid(row=0, column=1, pady= 20, padx=20)

speler_label_3 = Label(speler_frame, text="", bg="#efa70c")
speler_label_3.grid(row=0, column=2, pady= 20, padx=20)

speler_label_4 = Label(speler_frame, text="", bg="#efa70c")
speler_label_4.grid(row=0, column=3, pady= 20, padx=20)

speler_label_5 = Label(speler_frame, text="", bg="#efa70c")
speler_label_5.grid(row=0, column=4, pady= 20, padx=20)

#frame voor de knoppen
knoppen_frame = Frame(window, bg="#efa70c")
knoppen_frame.pack(pady=20)

#knoppen
shuffle_knop = Button(knoppen_frame, text="Reset", font=("Helvetica", 14), command= shuffle, bg="#5d0303", fg="#efa70c", activebackground="#840707", activeforeground="#a27108")
shuffle_knop.grid(row= 0, column= 0, pady= 10, padx=5)

hit_knop = Button(knoppen_frame, text="Hit", font=("Helvetica", 14), command= speler_hit, bg="#5d0303", fg="#efa70c", activebackground="#840707", activeforeground="#a27108")
hit_knop.grid(row=0, column=1, pady=10, padx=5)

stand_knop = Button(knoppen_frame, text="Stand", font=("Helvetica", 14), command = stand, bg="#5d0303", fg="#efa70c", activebackground="#840707", activeforeground="#a27108")
stand_knop.grid(row=0, column=2, pady=10, padx=5)

shuffle()
window.mainloop()