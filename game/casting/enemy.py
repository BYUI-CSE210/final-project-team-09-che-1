import constants
from game.casting.actor import Actor


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
    
    def vanish(self, cast):
        """vanishes the enemy from the screen and the cast
        
        args:
            self: an instance of an enemy
            cast: the cast containing the actors
        """

        cast.remove_actor("enemies", self)





