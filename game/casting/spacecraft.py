import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Spacecraft(Actor):
    """A spacecraft in this game is the main player
    
    The responsability of the spacecraft is to move itself in 
    the screen avoinding lasers to survive
    
    Attributes:
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        super().__init__()
        self._color = constants.WHITE
    
    def get_player(self):

        return self.get_position()
    

    #def reset()