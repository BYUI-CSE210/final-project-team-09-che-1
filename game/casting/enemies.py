import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast


class Enemies(Actor):
    """An artifact in this game could be a rock or a gem
    
    The responsability of the artifact is to keep track of the 
    score earned by the player
    
    Attributes:
        score (int) = the score earned depending if the character is a gem or a rock
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        super().__init__()
    
    def get_enemies(self):

        for n in range(constants.DEFAULT_ARTIFACTS):
            enemies = random.choice(constants.ENEMIES)

            x = random.randint(1, constants.COLS - 1)
            y = random.randint(1, 15)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            cast = Cast()
            enemy = Enemies()
            enemy.set_text(enemies)
            enemy.set_font_size(constants.FONT_SIZE)
            enemy.set_color(color)
            enemy.set_position(position)
            enemy.set_velocity(constants.ENEMIES_VELOCITY)
            cast.add_actor("ENEMIES", enemy)