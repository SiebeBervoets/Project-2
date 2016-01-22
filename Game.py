from random import randint
from threading import Thread
import os, pygame
from Player import *
from Tile import *
from Common import *
from Node import *
import time



###COLORS
white = 255, 255, 255
red = 225, 0, 0
green = 0, 225, 0
blue = 0, 0, 255
yellow = 105, 75, 50
black = (0,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()


size = width,height = 1000, 900
display_width=1000
display_height=900

screen = pygame.display.set_mode(size)
canvas=pygame.display.get_surface()
camera1=pygame.Rect(0,0,700,700)
camera2=pygame.Rect(20,700,660,180)
camera3=pygame.Rect(700,20,280,660)
camera4=pygame.Rect(700,700,280,180)

pygame.display.set_caption('Survivor by group 1')
GameIcon=pygame.image.load("Content/_fight.png").convert()
pygame.display.set_icon(GameIcon)

dobbel1=pygame.image.load('Content\Dobbel_1.png').convert()
dobbel2=pygame.image.load('Content\Dobbel_2.png').convert()
dobbel3=pygame.image.load('Content\Dobbel_3.png').convert()
dobbel4=pygame.image.load('Content\Dobbel_4.png').convert()
dobbel5=pygame.image.load('Content\Dobbel_5.png').convert()
dobbel6=pygame.image.load('Content\Dobbel_6.png').convert()

offset = 60
board_size = 11
Board, p1, p2, p3, p4= build_square_matrix(board_size, offset)



## CONSTRUCTORS




##PRINTS




##Pre-Game




##Game Elements






##Loops
def game_intro():
    pygame.mixer.music.load("Content/Rocky Theme Tune (8 Bit Remix).mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1000,0)
    gameDisplay.fill(white)
    bg = pygame.image.load("Content/boxing glove 2.jpg")
    ab = pygame.image.load("Content/boxing glove.jpg")

    bg = pygame.transform.scale(bg, (400, 425))
    ab = pygame.transform.scale(ab, (400, 425))

    gameDisplay.blit(bg, (475, 150))
    gameDisplay.blit(ab, (125, 150))

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        largeText = pygame.font.SysFont("felixtitling",115)
        TextSurf, TextRect = text_objects("Survivor", largeText)
        TextRect.center = ((display_width/2),(display_height/10))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start Game",25,600,150,50,green,bright_green,game_loop)
        st = pygame.image.load("Content/start game button.png")
        st = pygame.transform.scale(st, (150, 50))
        gameDisplay.blit(st, (25, 600))

        button("Quit Game",825,600,150,50,red,bright_red,quitgame)
        quit = pygame.image.load("Content/quit button.png")
        quit = pygame.transform.scale(quit, (150, 50))
        gameDisplay.blit(quit, (825, 600))

        button("Help",560,600,150,50,green,bright_green,help_loop)
        hel = pygame.image.load("Content/help button.png")
        hel = pygame.transform.scale(hel, (150, 50))
        gameDisplay.blit(hel, (560, 600))

        button("settings",290,600,150,50,green,bright_green,settings)
        set = pygame.image.load("Content/settings button.png")
        set = pygame.transform.scale(set, (150, 50))
        gameDisplay.blit(set, (290, 600))


        pygame.display.update()
        clock.tick(15)

def settings():
    global pause
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("verdana",70)
    TextSurf, TextRect = text_objects("settings", largeText)
    TextRect.center = ((display_width/6),(display_height/10))
    gameDisplay.blit(TextSurf, TextRect)


    close_down = False


    while not close_down:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("back",25,500,150,50,green,bright_green,game_intro)
        back = pygame.image.load("Content/back button.png")
        back = pygame.transform.scale(back, (150, 50))
        gameDisplay.blit(back, (25, 500))
        button("player amount",25,150,150,50,white,white,)

        button("2",320,150,75,50,red,white)
        one = pygame.image.load("Content/1.png")
        one = pygame.transform.scale(one, (75, 50))
        gameDisplay.blit(one, (320, 150))

        button("3",445,150,75,50,red,white)
        two = pygame.image.load("Content/2.png")
        two = pygame.transform.scale(two, (75, 50))
        gameDisplay.blit(two, (445, 150))

        button("4",570,150,75,50,red,white)
        tri = pygame.image.load("Content/3.png")
        tri = pygame.transform.scale(tri, (75, 50))
        gameDisplay.blit(tri, (570, 150))

        button("5",695,150,75,50,red,white)
        fou = pygame.image.load("Content/4.png")
        fou = pygame.transform.scale(fou, (75, 50))
        gameDisplay.blit(fou, (695, 150))

        pygame.display.update()
        clock.tick(60)



def help_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)



    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)

        largeText = pygame.font.SysFont("comicsansms",80)
        TextSurf, TextRect = text_objects("Spelregels", largeText)
        TextRect.center = ((display_width/2),(30))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("1. Diegene die het hoogst gooit begint met het spel.", largeText)
        TextRect.center = ((184),(100))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("2. Elke speler heeft zijn eigen hoek (3 vakjes) en start vanaf die hoek met de klok mee.", largeText)
        TextRect.center = ((298),(120))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("3. Elke speler begint met 100 Levenspunten en 15 Conditiepunten.", largeText)
        TextRect.center = ((232),(140))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("4. Elke speler heeft een Scorekaart van zijn Character en een bijpassende pion (bokshandschoen).", largeText)
        TextRect.center = ((331),(160))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("5. Er wordt gedobbeld om voort te bewegen over het bordspel.", largeText)
        TextRect.center = ((219),(180))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("6. Wanneer een speler op een vakje ‘Fight!’ terechtkomt moet deze vechten tegen de Superfighter ongeacht of er een speler ook op dat vakje staat.", largeText)
        TextRect.center = ((490),(200))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("7. De Superfighter wordt bepaald door een Superfighter-kaart van de stapel op het bordspel te pakken. Leg deze hierna weer onderaan de stapel.", largeText)
        TextRect.center = ((486),(220))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("8. Dobbelen geeft, aan de hand van de Scorekaart, een schade aan met de bijbehorende Conditiepunten.", largeText)
        TextRect.center = ((349),(240))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("9. Wanneer men geen Conditiepunten meer heeft kan er géén schade aan de tegenstander worden gedaan!", largeText)
        TextRect.center = ((356),(260))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("10. Wanneer er gevochten moet worden en beide spelers geen Conditiepunten hebben ontvangt de verdediger 15 schade.", largeText)
        TextRect.center = ((396),(280))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("11. De hoogste schade - de laagste schade = schade aan de speler met de laagste schade.", largeText)
        TextRect.center = ((293),(300))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("12. Wanneer 2 spelers op hetzelfde vak komen wordt er tegen elkaar gevochten. Meer dan 2 spelers op één vak?", largeText)
        TextRect.center = ((372),(320))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("Dan kiest de diegene die als laatste op het vak terecht is gekomen een tegenstander die ook op het vak staat.", largeText)
        TextRect.center = ((382),(340))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("13. Wanneer je beide op een ‘Fight!’ vak terechtkomt wordt er alleen gevochten met de Superfighter en niet met elkaar.", largeText)
        TextRect.center = ((393),(360))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("14. Je ontvangt 15 Conditiepunten als je langs je eigen hoek komt(max = 15 Conditiepunten).", largeText)
        TextRect.center = ((309),(380))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("15. Je ontvangt 10 Levenspunten als je op je eigen hoek komt.", largeText)
        TextRect.center = ((208),(400))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("16. Je kan je Levenspunten bijhouden aan de hand van het kladblok dat is bijgeleverd.", largeText)
        TextRect.center = ((284),(420))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("17. Wanneer een hoek leeg is wordt er -10 Levenspunten gerekend. Met 2 of 3 spelers heb je dus een lege hoek.", largeText)
        TextRect.center = ((370),(440))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("Ook wanneer iemand af is heb je een lege hoek.", largeText)
        TextRect.center = ((184),(460))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("Times New Roman",16)
        TextSurf, TextRect = text_objects("18. Verwijder je pion wanneer je geen Levenspunten meer hebt. Je hebt verloren.", largeText)
        TextRect.center = ((267),(480))
        gameDisplay.blit(TextSurf, TextRect)

        button("Back",150,500,150,50,green,bright_green,game_intro)
        # button("Back to menu",350,500,150,50,green,bright_green,game_intro)
        button("Quit Game",550,500,150,50,red,bright_red,quitgame)



        pygame.display.update()
        clock.tick(60)
