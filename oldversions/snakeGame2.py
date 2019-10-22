##Snake Game2! - Prototype!
import math
import pygame
from pygame.locals import *
import random
import sys
###The Training Code challenge 3, youtube
###https://github.com/TheAILearner/Snake-Game-with-Pygame/blob/master/snake%20game%20with%20pygame.ipynb
###https://theailearner.com/2018/10/06/creating-a-snake-game-with-pygame/
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
pygame.display.set_caption('Snake')
class Game():
    def __init__(self):
        self.snake = Snake() #snake obj
        self.food = Food() #food obj

    def play_game(self):
        self.snake.move()
        self.snake.draw()
        self.food.draw()
        self.snake.eat(self.food)
        self.display_score()
        self.crashes()

    def new_game(self):
        self.snake = Snake()
        self.snake.eaten = 0
        self.snake.position = [[self.snake.x, self.snake.y],
                               [self.snake.x-SCALE, self.snake.y],
                               [self.snake.x-(2*SCALE), self.snake.y]]
        self.snake.head = [self.snake.x, self.snake.y]
        self.snake.pbd = self.snake.RIGHT
        self.snake.bd = self.snake.RIGHT

    def display_score(self):
        font = pygame.font.SysFont(None, 40)
        text = font.render('Score: ' + str(self.snake.eaten), True, BLACK)
        DISPLAYSURF.blit(text,(0,0))

    def crashes(self):
        if self.snake.crash() == True:
            print('GAME OVER')
            self.new_game()


class Snake():
    def __init__(self, x=(2*SCALE), y=(2*SCALE)):
        self.x = x
        self.y = y
        self.eaten = 0
        self.position = [[self.x, self.y],
                         [self.x-SCALE, self.y],
                         [self.x-(2*SCALE), self.y]]
        self.head = [self.x, self.y]
        self.UP = 'up'
        self.DOWN = 'down'
        self.RIGHT = 'right'
        self.LEFT = 'left'
        self.pbd = self.RIGHT
        self.bd = self.RIGHT


    def move(self):
        '''Sets movement direction based on key press (WASD controlls)'''
        ##Changes direction based on button pressed -- sets self.bd (direction snake goes in @all times)
        ##Limits snake from going back into itself
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a or event.key == K_LEFT) and self.pbd != self.RIGHT:
                self.bd = self.LEFT
            elif (event.key == pygame.K_d or event.key == K_RIGHT) and self.pbd != self.LEFT:
                self.bd = self.RIGHT
            elif (event.key == pygame.K_w or event.key == K_UP) and self.pbd != self.DOWN:
                self.bd = self.UP
            elif (event.key == pygame.K_s or event.key == K_DOWN) and self.pbd != self.UP:
                self.bd = self.DOWN
            else:
                self.bd = self.bd

        ##Code that makes the snake always moves in direction its told.
        if self.bd == self.RIGHT:
            self.head[0] += SCALE
        elif self.bd == self.LEFT:
            self.head[0] -= SCALE
        elif self.bd == self.DOWN:
            self.head[1] += SCALE
        elif self.bd == self.UP:
            self.head[1] -= SCALE
        else:
            pass
        self.pbd = self.bd

        ##snakes movement, by removing tail and adding another spot infront of the head.
        self.position.insert(0, list(self.head))
        self.position.pop()

    def crash(self):
        '''Ends the game if snake head goes off screen into boundry, or runs into itself'''
        if self.head[0] < 0 or self.head[0] > DIS_X or self.head[1] < 0 or self.head[1] > DIS_Y:
            return True
        elif [self.head[0],self.head[1]] in self.position[2:]:
            return True
        else:
            return False

    def draw(self):
        for position in self.position:
            pygame.draw.rect(DISPLAYSURF, RED, (position[0], position[1],SCALE,SCALE))

    def eat(self, apple_pos):
        '''If snake head, collides with apple, increment score,
        create new apple and increase size of snake'''
        if self.head[0] == apple_pos.x and self.head[1] == apple_pos.y:
            self.eaten += 1
            ##print('EATING: ' + str(self.eaten))
            apple_pos.new_food() ##add new piece of food
            ##print(self.position)
            self.position.insert(0, list(self.head))##add new segment to snake
            return True


class Food():
    def __init__(self):
        '''initialize x, y values of the 1st piece of food'''
        self.x = self.pick_location(DIS_X)
        self.y = self.pick_location(DIS_Y)

    def draw(self):
        '''Draws the initial/starting piece of food on the screen'''
        pygame.draw.rect(DISPLAYSURF, PURPLE, (self.x, self.y,SCALE,SCALE))

    def pick_location(self, size):
        '''Size: Size of screen, to pick a value x,y that fits inside of the size of screen'''
        value = random.randint(SCALE, (size-SCALE))
        return math.floor((value/SCALE))*SCALE

    def new_food(self):
        '''Resets the x, y values for the food, and draws new piece of food on screen'''
        self.x = self.pick_location(DIS_X)
        self.y = self.pick_location(DIS_Y)
        pygame.draw.rect(DISPLAYSURF, PURPLE, (self.x, self.y, SCALE, SCALE))


##Other Code outside of main game loop---------------------------------------------------
g = Game()

####--MAIN LOOP--------------------------------------------------------------------------
while True:
    ##Event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ##Drawing Surface Stuff
    DISPLAYSURF.fill(_BGCOLOR)
    g.play_game()

    pygame.display.update()
    fps_clock.tick(FPS)
