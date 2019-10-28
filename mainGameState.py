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
        #self.snake = Snake()
        self.snake.x, self.snake.y = START_X, START_Y
        self.snake.color = SNAKE_COLOR
        self.snake.eaten = 0
        self.snake.position = [[self.snake.x, self.snake.y],
                               [self.snake.x-SCALE, self.snake.y],
                               [self.snake.x-(2*SCALE), self.snake.y]]
        self.snake.head = [self.snake.x, self.snake.y]
        self.snake.previous_direction = self.snake.RIGHT
        self.snake.direction = self.snake.RIGHT
        self.food.x = self.food.pick_location(DIS_X)
        self.food.y = self.food.pick_location(DIS_Y)

    def display_score(self, screen):
        font = pg.font.SysFont(None, 40)
        text = font.render('Score: ' + str(self.snake.eaten), True, BLACK)
        screen.blit(text,(0,0))

    def display_gameover(self, screen):
        font = pg.font.SysFont(None, 100)
        text = font.render('GAME OVER!', True, BLACK)
        text_rect = text.get_rect(center=(DIS_X, DIS_Y))
        screen.blit(text,(text_rect))

    def crashes(self):
        if self.snake.crash() == True:
            self.snake.color = BLACK
            self.next = 'gameover'
            self.done = True
            self.new_game()

    def draw_background(self, screen):
        pg.draw.rect(screen, WHITE2, (BACKGROUND))


    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            self.next = 'pause'
            self.done = True
        elif event.type == pg.KEYDOWN:
            self.snake.move(event)
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)
        self.snake.snake_move()
        self.snake.eat(self.food, screen)
        self.crashes()

    def draw(self, screen):
        screen.fill((GRAY))
        self.draw_background(screen)
        self.snake.draw(screen)
        self.food.draw(screen)
        self.display_score(screen)
