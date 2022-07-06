import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast


class Enemy(Actor):
    """An Enemie in this game 
    
    The responsability of the enemy is to attack the main player
    
    Attributes:
        
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        super().__init__()
        self._color = constants.RED
    
    def get_player(self):

        return self.get_position()





