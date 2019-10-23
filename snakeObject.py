'''
snakeObject.py - Main class for snake and food objects
'''
import math
import pygame as pg
from pygame.locals import *
from pyVariables import *
import random

'''SNAKE CLASS'''
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

    def snake_move(self):
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



    def move(self, event):
        '''Sets movement direction based on key press (WASD controlls)'''
        if (event.key == pg.K_a or event.key == K_LEFT) and \
                                        self.pbd != self.RIGHT:
            self.bd = self.LEFT
        elif (event.key == pg.K_d or event.key == K_RIGHT) and \
                                          self.pbd != self.LEFT:
            self.bd = self.RIGHT
        elif (event.key == pg.K_w or event.key == K_UP) and \
                                          self.pbd != self.DOWN:
            self.bd = self.UP
        elif (event.key == pg.K_s or event.key == K_DOWN) and \
                                          self.pbd != self.UP:
            self.bd = self.DOWN
        else:
            self.bd = self.bd

    def crash(self):
        '''Ends the game if snake head goes off screen into boundry, or runs into itself'''
        if self.head[0] < 0 or self.head[0] > DIS_X or self.head[1] < 0 or self.head[1] > DIS_Y:
            return True
        elif [self.head[0],self.head[1]] in self.position[2:]:
            return True
        else:
            return False

    def draw(self, screen):
        for position in self.position:
            pg.draw.rect(screen, RED, (position[0], position[1],SCALE,SCALE))

    def eat(self, apple_pos, screen):
        '''If snake head, collides with apple, increment score,
        create new apple and increase size of snake'''
        if self.head[0] == apple_pos.x and self.head[1] == apple_pos.y:
            self.eaten += 1
            apple_pos.new_food(screen) ##add new piece of food
            self.position.insert(0, list(self.head))##add new segment to snake
            return True


class Food():
    def __init__(self):
        '''initialize x, y values of the 1st piece of food'''
        self.x = self.pick_location(DIS_X)
        self.y = self.pick_location(DIS_Y)


    def draw(self, screen):
        '''Draws the initial/starting piece of food on the screen'''
        pg.draw.rect(screen, PURPLE, (self.x, self.y,SCALE,SCALE))

    def pick_location(self, size):
        '''Size: Size of screen, to pick a value x,y that fits inside of the size of screen'''
        value = random.randint(SCALE, (size-SCALE))
        return math.floor((value/SCALE))*SCALE

    def new_food(self, screen):
        '''Resets the x, y values for the food, and draws new piece of food on screen'''
        self.x = self.pick_location(DIS_X)
        self.y = self.pick_location(DIS_Y)
        self.draw(screen)
