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
    def __init__(self, x=START_X, y=START_Y):
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
        self.previous_direction = self.RIGHT
        self.direction = self.RIGHT
        self.color = SNAKE_COLOR


    def snake_move(self):
        if self.direction == self.RIGHT:
            self.head[0] += SCALE
        elif self.direction == self.LEFT:
            self.head[0] -= SCALE
        elif self.direction == self.DOWN:
            self.head[1] += SCALE
        elif self.direction == self.UP:
            self.head[1] -= SCALE
        else:
            pass
        self.previous_direction = self.direction
        self.position.insert(0, list(self.head))
        self.position.pop()

    def move(self, event):
        '''Sets movement direction based on key press (WASD/ARROW controls)'''
        if (event.key == pg.K_a or event.key == K_LEFT) and \
                                    self.previous_direction != self.RIGHT:
            self.direction = self.LEFT
        elif (event.key == pg.K_d or event.key == K_RIGHT) and \
                                      self.previous_direction != self.LEFT:
            self.direction = self.RIGHT
        elif (event.key == pg.K_w or event.key == K_UP) and \
                                      self.previous_direction != self.DOWN:
            self.direction = self.UP
        elif (event.key == pg.K_s or event.key == K_DOWN) and \
                                      self.previous_direction != self.UP:
            self.direction = self.DOWN
        else:
            self.direction = self.direction

    def crash(self):
        '''Checks to see if the snake has crashed'''
        if self.head[0] < LEFT_BOUND_X or self.head[0] > RIGHT_BOUND_X or \
           self.head[1] < TOP_BOUND_Y  or self.head[1] > BOTTOM_BOUND_Y:
            return True
        elif [self.head[0],self.head[1]] in self.position[2:]:
            return True
        else:
            return False

    def draw(self, screen):
        for position in self.position:
            pg.draw.rect(screen, self.color,
                        (position[0], position[1],SCALE-1,SCALE-1))

    def eat(self, apple_pos, screen):
        '''
        If snake head, collides with apple, increment score,
        create new apple and increase size of snake
        '''
        if self.head[0] == apple_pos.x and self.head[1] == apple_pos.y:
            self.eaten += 1
            '''add new piece to head'''
            self.position.insert(0, list(self.head))
            '''adds 3 pieces to tail'''
            for i in range(3):
                self.y = -50 #So that GREEN square doesn't appear on screen
                self.position.append([self.x - (len(self.position)+1 * SCALE),
                                      self.y - (len(self.position)+1 * SCALE)])
            apple_pos.new_food(screen, self.position)
            return True


class Food():
    def __init__(self):
        '''initialize x, y values of the 1st piece of food'''
        self.x = int()
        self.y = int()
        self.first_food()
        self.possible_food_location = []



    def draw(self, screen):
        '''Draws the initial/starting piece of food on the screen'''
        pg.draw.rect(screen, FOOD_COLOR, (self.x, self.y,SCALE-1,SCALE-1))

    def new_food(self, screen, snake_location):
        '''Sets x, y of food based on open board locations'''
        self.calculate_possible_location(snake_location)
        self.x, self.y = random.choice(self.possible_food_location)
        self.draw(screen)

    def first_food(self):
        '''Create random location for the 1st food, away from top left corner'''
        x = random.randint((LEFT_BOUND_X + (6*SCALE)), RIGHT_BOUND_X)
        y = random.randint((TOP_BOUND_Y + (6*SCALE)), BOTTOM_BOUND_Y)
        self.x = math.floor((x/SCALE)) * SCALE
        self.y = math.floor((y/SCALE)) * SCALE

    def calculate_possible_location(self, snake_location):
        '''Calcualate board locations that doesn't contain the snake'''
        self.possible_food_location = []
        for i in range(LEFT_BOUND_X, RIGHT_BOUND_X, SCALE):
            for j in range(TOP_BOUND_Y, BOTTOM_BOUND_Y, SCALE):
                if [i,j] not in snake_location:
                    self.possible_food_location.append([i,j])
