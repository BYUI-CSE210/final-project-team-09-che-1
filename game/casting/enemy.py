import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast


class Enemy(Actor):
    """An Enemy in this game is represented a by a text character, it tries to
    defeat the player by shooting lasers or touching the screen bottom

    The responsability of the enemy is to attack the main player while
    moving downwards
    
    Attributes:
        _color (color) = the color of the enemy
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        
        super().__init__()
        self._color = constants.RED
    
    def get_enemy(self):
        """gets the enemy's position on the screen
        
        args: an instance of an enemy
        """

        return self.get_position()
    
    def vanish(self, cast):
        """vanishes the enemy from the screen and the cast
        
        args:
            self: an instance of an enemy
            cast: the cast containing the actors
        """

        cast.remove_actor("enemies", self)





