from game.shared.color import Color
from game.shared.point import Point

#GAME
GAME_NAME = "Space Invaders"
DEFAULT_LIVES = 3
FRAME_RATE = 45

#SCREEN 
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
COLUMNS = 60 
ROWS = 40
CELL_SIZE = 15
FONT_SIZE = 15

#COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)

#ENEMIES
DEFAULT_ARTIFACTS = 70
ENEMIES = ["*", "o",]
ENEMIES_VELOCITY = Point(0, 5)
