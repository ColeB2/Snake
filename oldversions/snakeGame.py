##Snake Game!
import pygame
import sys
from pygame.locals import *
import random
import math
'''Snake Game prototype'''
##--COLORS-------------------------------------------------------------------------------
##AQUA, BLACK, BLUE, FUCHSIA, GRAY, GREEN, LIME, MAROON, NAVE_BLUE, OLIVE, PURPLE,
##RED, SILVER, TEAL, WHITE, YELLOW, BLACK
from pyColor import *
_BGCOLOR = (230, 230, 250)
##initialize pygame----------------------------------------------------------------------
pygame.init()
##Frame Rate Settings--------------------------------------------------------------------
FPS = 10
fps_clock = pygame.time.Clock()
##Creating a window----------------------------------------------------------------------
DIS_X = 600
DIS_Y = 600
DIS_SIZE = (DIS_X,DIS_Y)
DISPLAYSURF = pygame.display.set_mode(DIS_SIZE)
#####BOARD SCALE-------------------------------------------------------------------------
SCALE = 20
##Window top bar caption-----------------------------------------------------------------
pygame.display.set_caption('Display Caption Name')
##--CLASSES--(here or in separate module-------------------------------------------------
class Segment:
    def __init__(self, x=(2*SCALE), y=(2*SCALE)):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, RED, (self.x, self.y,SCALE,SCALE))

class Snake(Segment):
    def __init__(self, x=(2*SCALE), y=(2*SCALE), xspeed=1, yspeed=0):
        self.x = x
        self.y = y
        self.xspeed = xspeed*SCALE
        self.yspeed = yspeed*SCALE
        self.size = 0
####        self.total = 0
####        self.tail = []

        self.position = [[self.x, self.y]]

    def update(self):
##        for i in range(self.total-1):
##            self.tail[i] = self.tail[i+1]
##
##        self.tail[self.total-1] = (self.x, self.y)
####        if self.total == len(self.tail):
####            for i in range(0, len(self.tail)):
####                #self.tail[i] = self.tail[i+1]
####                self.tail.insert(0, self.tail[i])
####
####
####            self.tail.append((self.x, self.y))




        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        ##Updating list of positions so that the segments can move.
##        for i in range(len(self.position)):
##            self.position[i][0] += self.xspeed
##            self.position[i][1] += self.yspeed

        #self.position = [(self.x, self.y)]
        print(self.position)
        ##connstraint on snake
        if self.x > DIS_X-(2*SCALE) or self.x < 0+SCALE or self.y < 0+SCALE or self.y >DIS_Y-(SCALE*2):
            self.xspeed = 0
            self.yspeed = 0

##    def new_seg(self):
##        while self.size > 0:
##            NEW = Segment()
##            NEW.draw()

    def move(self):
        '''Sets movement direction based on key press (WASD controlls)'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.xspeed = 0
                self.yspeed = -SCALE
            if event.key == pygame.K_s:
                self.xspeed = 0
                self.yspeed = SCALE
            if event.key == pygame.K_a:
                self.xspeed = -SCALE
                self.yspeed = 0
            if event.key == pygame.K_d:
                self.xspeed = SCALE
                self.yspeed = 0


    def draw(self):
##        for i in range(0,self.size):
##            pygame.draw.rect(DISPLAYSURF, RED, (self.position[i][0], self.position[i][1],SCALE,SCALE))
##        for i in range(0,self.total):
##            pygame.draw.rect(DISPLAYSURF, RED, (self.tail[i][0], self.tail[i][1],SCALE,SCALE))



        pygame.draw.rect(DISPLAYSURF, RED, (self.x, self.y,SCALE,SCALE))

    def eat(self, pos):
        if self.x == pos.x and self.y == pos.y:
            ##self.total += 1
            ##print('EATING: ' + str(self.total))
            self.size += 1
##            self.position.insert(0,
##                                 [self.position[0][0]-SCALE, self.position[0][1]])
            print('Eating: ' + str(self.size))

            pos.new_food()

            ##print(self.tail)
            print(self.position)
            #self.add_length(pos.x, pos.y)




class Food:
    def __init__(self):
        self.x = self.pick_location(DIS_X)
        self.y = self.pick_location(DIS_Y)

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, PURPLE, (self.x, self.y,SCALE,SCALE))

    def pick_location(self, size):
        value = random.randint(SCALE, (size-SCALE))
        return math.floor((value/SCALE))*SCALE

    def new_food(self):
        self.x = self.pick_location(DIS_X)
        self.y = self.pick_location(DIS_Y)
        pygame.draw.rect(DISPLAYSURF, PURPLE, (self.x, self.y, SCALE, SCALE))




##Other Code outside of main game loop---------------------------------------------------
s = Snake()
#f = Food(random.randint((SCALE*2),DIS_X-(SCALE*2)),random.randint((SCALE*2),DIS_Y-(SCALE*2)))
f = Food()

####--MAIN LOOP--------------------------------------------------------------------------
while True:
    ##Event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ##S Controls

    ##Drawing Surface Stuff
    DISPLAYSURF.fill(_BGCOLOR)
    s.update()
    s.move()
    s.draw()
    f.draw()
    s.eat(f)



    pygame.display.update()
    fps_clock.tick(FPS)
