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
