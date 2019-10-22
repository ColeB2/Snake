'''
gameStates.py
'''
import pygame as pg
from pyVariables import *
import sys

class States():
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'

    def cleanup(self):
        print('cleaning up Menu state stuff')

    def startup(self):
        print('starting Menu state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((255,0,0))

class Pause(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'

    def cleanup(self):
        print('cleaning up Pause state stuff')

    def startup(self):
        print('starting Pause state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            self.next = 'game'
            self.done = True
        elif event.type == pg.KEYDOWN:
            print('Pause State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((128,128,128))
'''
class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'


    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            print('Pause State keydown')
            self.next = 'pause'
            self.done = True
        elif event.type == pg.KEYDOWN:    print('Game State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((0,0,255))
'''
class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()


    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()

'''
settings = {
    'size': DISPLAYSURF,
    'fps' : FPS
}

app = Control(**settings)
state_dict = {
    'menu': Menu(),
    'game': Game(),
    'pause': Pause()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pg.quit()
sys.exit()
'''
