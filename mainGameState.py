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
        self.high_score = self.snake.eaten


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
        self.food.first_food()

    def display_score(self, screen):
        font = pg.font.SysFont(None, 40)
        text = font.render('Score: ' + str(self.snake.eaten), True, BLACK)
        text_rect = text.get_rect(bottomleft=(BACK_X,BACK_Y) )
        screen.blit(text, text_rect)

    def calculate_high_score(self):
        if self.snake.eaten > self.high_score:
            self.high_score = self.snake.eaten
        elif self.high_score > self.snake.eaten:
            self.high_score = self.high_score

    def display_high_score(self, screen):
        self.calculate_high_score()
        font = pg.font.SysFont(None, 40)
        text = font.render('High Score: ' + str(self.high_score), True, BLACK)
        text_rect = text.get_rect(bottomright=(RIGHT_BOUND_X, BACK_Y))
        screen.blit(text, text_rect)

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
        self.display_high_score(screen)
