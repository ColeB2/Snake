'''
main.py - main game file, runs the game
'''
from gameStates import *
from mainGameState import Game

if __name__ == '__main__':
    settings = {
        'size': DIS_SIZE,
        'fps' : FPS
    }
    pg.init()
    app = Control(**settings)
    state_dict = {
        'menu': Menu(),
        'game': Game(),
        'pause': Pause(),
        'gameover': Game_Over()
    }

    app.setup_states(state_dict, 'menu')
    app.main_game_loop()
    pg.quit()
    sys.exit()
