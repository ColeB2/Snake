'''
snakeGameState.py - Has the game state, and the snake objects to create the
the game of Snake!
'''
'''GAMESTATE IMPORTS'''
from gameStates import States
import pygame as pg
from pyVariables import *

'''SNAKE/FOOD IMPORT'''
from snakeObject import *


class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.snake = Snake()
        self.food = Food()


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
        self.snake.snake_move()
        self.snake.eat(self.food, screen)
        self.crashes()

    def draw(self, screen):
        screen.fill((WHITE2))
        self.snake.draw(screen)
        self.food.draw(screen)
        self.display_score(screen)
