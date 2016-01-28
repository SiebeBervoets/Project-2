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
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    global pause
    largeText = pygame.font.SysFont("verdana",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    canvas.blit(TextSurf, TextRect)
    pause=True

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        Clock.tick(15)

def button(msg, x, y, w, h, ic, ac, action=None, a=None, b=None, c=None, d=None, e=None, f=None, g=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (mouse[0] < x + w and mouse[0] > x) and (mouse[1] < y + h and mouse[1] > y):
        pygame.draw.rect(canvas, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if g != None:
                action(a, b, c, d, e, f, g)
            elif f != None:
                action(a, b, c, d, e, f)
            elif e != None:
                action(a, b, c, d, e)
            elif d != None:
                action(a, b, c, d)
            elif c != None:
                action(a, b, c)
            elif b != None:
                action(a, b)
            elif a != None:
                action(a)
            else:
                action()
    else:
        pygame.draw.rect(canvas, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("verdana", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    canvas.blit(textSurf, textRect)
    
##PRINTS
def Reprint():
    global loops
    screen.fill(black)
    Board.Reset(loops)
    Board.Draw(screen)
    canvas.fill((255,255,255),camera2)
    canvas.fill((255,255,255),camera3)
    canvas.fill((255,255,255),camera4)
    loops+=1

def Move_print(a, b, c, d):
    player=beurt.Value
    _width=int(34)
    while a+b+c+d !=0:
        if a>0:
            a-=1
            X_plus_move = _width
            for i in range(_width*2-7):
                   Reprint()
                   if player.Kleur ==1:
                       print_players(0,1,1,1)
                   elif player.Kleur == 2:
                       print_players(1,0,1,1)
                   elif player.Kleur==3:
                       print_players(1,1,0,1)
                   elif player.Kleur==4:
                       print_players(1,1,1,0)
                   screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                                (X_plus_move + player.Locatie.Position.X * offset,
                                 _width + player.Locatie.Position.Y * offset))
                   X_plus_move+=1
                   pygame.display.update(camera1)

        elif b>0:
            b-=1
            Y_plus_move = _width
            for i in range(_width*2-7):
                   Reprint()
                   if player.Kleur ==1:
                       print_players(0,1,1,1)
                   elif player.Kleur == 2:
                       print_players(1,0,1,1)
                   elif player.Kleur==3:
                       print_players(1,1,0,1)
                   elif player.Kleur==4:
                       print_players(1,1,1,0)
                   screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                                (_width + player.Locatie.Position.X * offset,
                                Y_plus_move + player.Locatie.Position.Y * offset))
                   Y_plus_move+=1
                   pygame.display.update(camera1)
        elif c>0:
            c-=1
            X_min_move = _width
            for i in range(_width*2-7):
                   Reprint()
                   if player.Kleur ==1:
                       print_players(0,1,1,1)
                   elif player.Kleur == 2:
                       print_players(1,0,1,1)
                   elif player.Kleur==3:
                       print_players(1,1,0,1)
                   elif player.Kleur==4:
                       print_players(1,1,1,0)
                   screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                                (X_min_move + player.Locatie.Position.X * offset,
                                _width + player.Locatie.Position.Y * offset))
                   X_min_move-=1
                   pygame.display.update(camera1)
        elif d>0:
            d-=1
            Y_min_move = _width
            for i in range(_width*2-7):
                   Reprint()
                   if player.Kleur ==1:
                       print_players(0,1,1,1)
                   elif player.Kleur == 2:
                       print_players(1,0,1,1)
                   elif player.Kleur==3:
                       print_players(1,1,0,1)
                   elif player.Kleur==4:
                       print_players(1,1,1,0)
                   screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                                (_width + player.Locatie.Position.X * offset,
                                Y_min_move + player.Locatie.Position.Y * offset))
                   Y_min_move-=1
                   pygame.display.update(camera1)
        Reprint()

def print_players(x,y,z,a):
    if x == 1:
        player1.Value.draw(screen,offset)
    if y == 1:
        player2.Value.draw(screen,offset)
    if z == 1:
        player3.Value.draw(screen,offset)
    if a == 1:
        player4.Value.draw(screen,offset)



##Pre-Game
def Player_select(aantal):
    global players,player1,player2,player3,player4
    players=Empty
    for i in range(4):
        if i == 0 and aantal > 0:
            name="Player1"
            players=Node(Player(name,1,p1,"Content/__pawn_blue.png"),players)
            player1=players
        elif i ==0 and aantal == 0:
            players=Node(Player("CPU-1",1,p1,"Content/__pawn_blue.png"),players)
            players.Value.Ai=True
            player1=players
        if i == 1 and aantal >1:
            name="Player2"
            players=Node(Player(name,2,p2,"Content/__pawn_yellow.png"),players)
            player2=players
        elif i==1 and aantal <=1:
            players=Node(Player("CPU-2",2,p2,"Content/__pawn_yellow.png"),players)
            players.Value.Ai=True
            player2=players
        if i == 2 and aantal>2:
            name="Player3"
            players=Node(Player(name,3,p3,"Content/__pawn_blue.png"),players)
            player3=players
        elif i==2 and aantal <=2:
            players=Node(Player("CPU-3",3,p3,"Content/__pawn_blue.png"),players)
            players.Value.Ai=True
            player3=players
        if i == 3 and aantal>3:
            name="Player4"
            players=Node(Player(name, 4, p4, "Content/__pawn_red.png"),players)
            player4=players
        elif i==3 and aantal<=3:
            players=Node(Player("CPU-4",4,p4,"Content/__pawn_red.png"),players)
            players.Value.Ai=True
            player4=players


##Game Elements
def Change_turn(x):
    global players,beurt
    beurt=x.Tail
    time.sleep(1)
    if beurt.IsEmpty :
        beurt = players
    pygame.display.update(camera4)

def Bewegen(player):
    global beurt
    x=Rol()
    if x==1:
        canvas.blit(dobbel1,[780,735])
    elif x==2:
        canvas.blit(dobbel2,[780,735])
    elif x==3:
        canvas.blit(dobbel3,[780,735])
    elif x==4:
        canvas.blit(dobbel4,[780,735])
    elif x==5:
        canvas.blit(dobbel5,[780,735])
    else:
        canvas.blit(dobbel6,[780,735])
    pygame.display.update(camera4)

    for i in range(x):
        if player.Locatie.Next==1 or player.Locatie.Position == "(0,0)" :
            Move_print(1,0,0,0)
            player.Richting=1
            player.Locatie=player.Locatie.Right
        elif player.Locatie.Next==2 or player.Locatie.Position == "(10,0)" :
            Move_print(0,1,0,0)
            player.Richting=2
            player.Locatie=player.Locatie.Down
        elif player.Locatie.Next==3 or player.Locatie.Position == "(10,10)" :
            Move_print(0,0,1,0)
            player.Richting=3
            player.Locatie=player.Locatie.Left
        elif player.Locatie.Next==4 or player.Locatie.Position == "(0,10)" :
            Move_print(0,0,0,1)
            player.Richting=4
            player.Locatie=player.Locatie.Up
        else:
            if player.Richting == 1:
                Move_print(1, 0, 0, 0)
                player.Locatie=player.Locatie.Right
            elif player.Richting == 2:
                Move_print(0,1,0,0)
                player.Locatie=player.Locatie.Down
            elif player.Richting == 3:
                Move_print(0,0,1,0)
                player.Locatie=player.Locatie.Left
            elif player.Richting == 4:
                Move_print(0,0,0,1)
                player.Locatie=player.Locatie.Up
        Reprint()
        if i!=x:
            time.sleep(0.75)
        else:
            time.sleep(2.5)
        print_players(1,1,1,1)
        pygame.display.update(camera1)



gameDisplay = pygame.display.set_mode((display_width,display_height))

## FIGHT
def Player_attack_fight(starter, target, first_roll=None, choice=None):
    if first_roll == None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quitgame()
                    if event.key == pygame.K_h:
                        help_loop()
                    if event.key == pygame.K_SPACE:
                        Bewegen(beurt.Value)

            button("Gooi dobbelsteen", 40, 720, 200, 140, red, green, Player_attack_fight, starter, target, True)
            pygame.display.flip()
            clock.tick(10)

    ## TODO print keuzes
    elif choice == None:
        x = Rol()
        print(first_roll)
        time.sleep(1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quitgame()
                    if event.key == pygame.K_h:
                        help_loop()
                    if event.key == pygame.K_SPACE:
                        Bewegen(beurt.Value)

            canvas.fill((255, 255, 255), camera2)
            button("keuze 1", 40, 725, 200, 40, red, green, Player_attack_fight, starter, target, x, 0)
            button("keuze 2", 40, 770, 200, 40, red, green, Player_attack_fight, starter, target, x, 1)
            button("keuze 3", 40, 815, 200, 40, red, green, Player_attack_fight, starter, target, x, 2)
            pygame.display.flip()
            clock.tick(10)

    dmg = target.Value.Damage[first_roll - 1][choice]
    target.Value.Conditie -= target.Value.Damage[first_roll - 1][choice + 3]
    # time.sleep(5)
    y = Rol()
    # print rol
    # time.sleep(5)
    z = randint(0, 2)
    starter_dmg = starter.Damage[y - 1][z]
    starter.Conditie -= starter.Damage[y - 1][z + 3]
    # print dmg
    # print berekening
    Calc_parameters(starter, target, starter_dmg, dmg)


##Returns
def Return_same_location(List, player_location, player_kleur):
    locations = []
    while not List.IsEmpty:
        if List.Value.Locatie.Position == player_location and List.Value.Kleur != player_kleur:
            locations.append(List.Value.Locatie.Position)
            return List, locations
        List = List.Tail
    return None, []


def Return_random_element(List):
    for i in range(randint(0, 17)):
        List = List.Tail
    return List
    
    
def Return_bepaalde_player(tile_kleur):
    if tile_kleur == 6:
        return player1
    elif tile_kleur == 7:
        return player2
    elif tile_kleur == 8:
        return player3
    else:
        return player4

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
        
def game_loop():
    global pause,loops,beurt,players
    players=Turn_list(players)
    beurt=players
    loops=0
    Reprint()
    print_players(1,1,1,1)
    pygame.display.flip()
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitgame()
                if event.key == pygame.K_h:
                    help_loop()
                    beurt = Turn_list(players)


        # print(1)
        Reprint()
        button("Gooi dobbelsteen",40,720,200,140,red,green,Bewegen,beurt.Value,)
        button("Stop beurt",280,720,200,140,red,green,Change_turn,beurt)
        print_players(1,1,1,1)
        pygame.display.update([camera1,camera2,camera3])
        if loops == 5:
            loops=0
        clock.tick(60)

Player_select(0)
game_intro()
