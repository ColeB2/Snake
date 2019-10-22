'''
snakeGameState.py - Has the game state, and the snake objects to create the
the game of Snake!
'''
'''GAMESTATE IMPORTS'''
from gameStates import States
import pygame as pg
from pyVariables import *

'''SNAKE/FOOD IMPORTS'''
import math
from pygame.locals import *
import random

class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.snake = Snake()
        self.food = Food()


    def play_game(self, screen):
        self.snake.snake_move()
        self.snake.eat(self.food, screen)
        self.crashes()

    def new_game(self):
        self.snake = Snake()
        self.snake.eaten = 0
        self.snake.position = [[self.snake.x, self.snake.y],[self.snake.x-SCALE, self.snake.y],[self.snake.x-(2*SCALE), self.snake.y]]
        self.snake.head = [self.snake.x, self.snake.y]
        self.snake.pbd = self.snake.RIGHT
        self.snake.bd = self.snake.RIGHT

    def display_score(self, screen):
        font = pg.font.SysFont(None, 40)
        text = font.render('Score: ' + str(self.snake.eaten), True, BLACK)
        screen.blit(text,(0,0))

    def crashes(self):
        if self.snake.crash() == True:
            print('GAME OVER')
            self.new_game()

    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            print('Pause State keydown')
            self.next = 'pause'
            self.done = True
        elif event.type == pg.KEYDOWN:
            print('Game State keydown')
            self.snake.move(event)
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)
        self.play_game(screen)

    def draw(self, screen):
        screen.fill((230,230,250))
        self.snake.draw(screen)
        self.food.draw(screen)
        self.display_score(screen)

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

            '''

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
        self.position.pop()'''

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
