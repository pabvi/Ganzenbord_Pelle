import pygame, random, easygui, time, variabelen
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import *  
from blackjackspel import blackjack

def radvanfortuin():
    global score
    #random woord kiezen uit 4 woorden met allemaal een andere weging
    opties = ["verder", "+1", "+10", "-10"]
    gekozen_woord = str(random.choices(opties, weights=(91, 3, 3, 3), k=1))

    print(gekozen_woord)
    #per woord dat random gekozen is is er een actie die gebeurd
    if gekozen_woord == "['verder']":
        posities[beurt] =+ 48  
        print("top je mag verder")
    elif gekozen_woord == "['+1']":
        score[beurt] =+ 1
        print("Je krijgt 1 punt er bij!") 
    elif gekozen_woord == "['+10']":
        score[beurt] =+ 10
        print("je krijgt 10 punten er bij!")
    elif gekozen_woord == "['-10']":
        if score[beurt] < 10:
            if score[beurt] == 0:
                print("Je had helaas geen punten dus je hoeft niks inteleveren")
            else:
                print(f"jammer je moet {score[beurt]} punten inleveren")
                score[beurt] =- score[beurt]
        else:
            score[beurt] =- 10
            print("Jammer je moet 10 punten inleveren")
    #Hoeveel punten de speler +- heeft gekregen
    print(f"Je score is nu {score[beurt]}")


#alle posities van elk vakje op het bord
vakjes = [
#start-10
[65,874], [207,874], [273,874], [273,808], [207,808], [136,808], [65,808], [65,743], [136,743], [207,743],
[273,743], 
#Blackjack
[455,743], 
# 12-25
[762,743], [846,743], [846,808], [846,874], [931,874], [931,808], [931,746], [1015,743], [1015,808],[1015,874],
[1100,874], [1100,808], [1100,743], [1185,743],
#Roulette
[1466,743],
#27-36
[1664, 743], [1747, 743], [1747, 677], [1747, 610], [1747, 545], [1664, 545], [1579, 545], [1495, 545], [1495, 479], 
#Slots
[1462, 414],
#38-58
[1490, 160], [1490, 94], [1409, 94], [1321, 94], [1236, 94], [1236, 160], [1236,227], [1184, 291], [1100,291], 
[1015,291], [1015,357], [1015,423], [931,423], [931,357], [931,291], [846,291], [846,357], [846,423], [760, 423],
[760, 357], [760,291],[676,291],
#Poker
[403,291],
#60-einde
[183,291], [38,291]
]

#speler karakters
bord = pygame.image.load("board.png")
speler0 = pygame.image.load("fisches/pokerp1.png")
speler1 = pygame.image.load("fisches/pokerp2.png")
speler2 = pygame.image.load("fisches/pokerp3.png")
speler3 = pygame.image.load("fisches/pokerp4.png")
speler4 = pygame.image.load("fisches/pokerp5.png")
speler5 = pygame.image.load("fisches/pokerp6.png")

done = False

posities = [0,0,0,0,0,0]

score = [10,10,10,10,10,10]

beurt = 0

worp = 0

winaar = -1

pygame.init()
  
WINDOW_SIZE = [1880,940]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Pelle's ganzenbordspel")

clock = pygame.time.Clock()

#main loop van het spel
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                worp = random.randint(1,6) 
                posities[beurt] += worp

                if posities[beurt] == 11:
                    ja_nee = messagebox.askyesno(title="Blackjack?", message="Wil je het blackjack spel spelen?", detail="Win= 10 fisches verlies= -10 fisches gelijkspel= +1 fische")
                    
                    if not ja_nee:
                        continue
                    else:
                        player_x = 455
                        player_y = 743
                        screen.blit(eval(f"speler{beurt}"), (player_x, player_y))
                        pygame.display.flip()
                        blackjack()
                        score[beurt] += variabelen.score
                        print(score[beurt])

                if posities[beurt] == 19:
                    ja_nee = messagebox.askyesno(title="Rad van fortuin?", message="Wil je het rad van fortuin draaien?", detail="Kans op route skip, +1 fische, +10 fisches en -10 fisches")
                    
                    if not ja_nee:
                        continue
                    else:
                        player_x = 1022
                        player_y = 764
                        screen.blit(eval(f"speler{beurt}"), (player_x, player_y))
                        pygame.display.flip()
                        radvanfortuin()

                if posities[beurt] >= 66:
                    posities[beurt] = 66
                    winaar = beurt

                else:    
                    if beurt < 5:
                        beurt += 1
                    else:
                        beurt = 0 

            
            elif event.key == pygame.K_BACKSPACE:
                posities = [0,0]
                beurt = 0
                winaar = -1


    clock.tick(30)
    pygame.display.flip()

    screen.fill((255,255,255))
    
    bordrect = bord.get_rect()
    screen.blit(bord,bordrect)

    for i in range (6):
        player_x = vakjes[posities[i]][0]
        player_y = vakjes[posities[i]][1]
        screen.blit(eval(f"speler{i}"), (player_x, player_y))
    
    myfont = pygame.font.SysFont(None, 40 )

    text ="laatste worp: " + str(worp)
    label = myfont.render(text, 1, (239, 167, 12))
    screen.blit(label, (150, 525))

    text = "Aan de beurt: speler " + str(beurt + 1)
    label = myfont.render(text, 1, (239, 167, 12))
    screen.blit(label, (500, 525))

pygame.quit()