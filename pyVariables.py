# pyColor.py
# list of python colors you commonly use.

AQUA = (0,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
FUCHSIA = (255,0,255)
GRAY = (128,128,128)
GREEN = (0,128,0)
LIME = (0,255,0)
MAROON = (128,0,0)
NAVY_BLUE = (0,0,128)
OLIVE = (128,128,0)
PURPLE = (128,0,128)
RED = (255,0,0)
SILVER = (192,192,192)
TEAL = (0,128,128)
WHITE = (255,255,255)
LAVENDER_MIST = (230,230,250)
YELLOW = (255,255,0)
LIGHT_GOLDENROD_YELLOW = (250,250,230)
SNAKE_GREEN = (56, 220, 5)
SNAKE_GREEN1 = (79, 250, 26)
SNAKE_GREEN2 = (110, 255, 65)


'''SCREEN SIZE'''
DIS_X = 800
DIS_Y = int(0.75*DIS_X)
DIS_SIZE = (DIS_X, DIS_Y)
'''PYGAME VARS'''
FPS = 15
'''SNAKE BOARD/BACKGROUND VARIABLES'''
SCALE = 20
TL_COORD = 3 * SCALE #TL - TOP LEFT
BACK_X = TL_COORD #BACK - Background
BACK_Y = TL_COORD
BACK_LENGTH = DIS_X - (2 * BACK_X) ##X value
BACK_HEIGHT = DIS_Y - (2 * BACK_Y) ##Y value
BACKGROUND = (BACK_X, BACK_Y, BACK_LENGTH, BACK_HEIGHT)
'''SCOREBOARD LOCATION'''
SCORE_X = BACK_X
SCORE_Y = DIS_Y - BACK_Y
HSCORE_X = DIS_X - BACK_X
HSCORE_Y = SCORE_Y
'''SNAKE BOUDNARIES'''
LEFT_BOUND_X = (BACK_X)
RIGHT_BOUND_X = DIS_X - LEFT_BOUND_X - SCALE
TOP_BOUND_Y = (BACK_Y)
BOTTOM_BOUND_Y = DIS_Y - TOP_BOUND_Y - SCALE
'''SNAKE VARIABLES'''
SNAKE_COLOR = SNAKE_GREEN
START_X = 2 * TL_COORD
START_Y = 2 * TL_COORD
'''FOOD VARIABLES'''
FOOD_COLOR = RED
'''PYTHON/PYGAME LOGOS'''
PYTHON_RECT = (100, DIS_Y - 150)
PYGAME_RECT = (DIS_X-350, DIS_Y-170)
'''PAUSE/GAMEOVER RECTANGLE SIZE'''
PAUSE_RECT = (BACK_X, BACK_Y, BACK_LENGTH , BACK_HEIGHT)
GAMEOVER_RECT = (DIS_Y/4,DIS_Y/4,DIS_X-300,DIS_Y-300)
