# Constants
TITLE = ""
SCREENRECT = SCREENWIDTH, SCREENHEIGHT = 480, 270
 
FPS = 60
FONT_NAME = "arial"
HS_FILE = "highscore.txt"

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 15

# platforms
PLATFORM_LIST = [
    (0, SCREENHEIGHT - 20, SCREENWIDTH, 20),
    (SCREENWIDTH // 2 - 40, SCREENHEIGHT // 2, 80, 20),
    (125, SCREENHEIGHT - 200, 100, 20),
    (305, 100, 180, 20),
    (100, 170, 60, 20)
]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)