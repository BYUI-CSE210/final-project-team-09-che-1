import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Spacecraft(Actor):
    """A spacecraft in this game is the main player
    
    The responsability of the spacecraft is to move itself in 
    the screen avoinding lasers to survive
    
    Attributes:
        _color (color): blue color to identify the spaceship
    """
    
    def __init__(self):
        """construct a new instance of a spacecraft"""   
        
        super().__init__()
        self._color = constants.BLUE
    
    def reset(self, cast): 
        """resets the player's into the middle of the screen
        
        args (self) = an instance of a spacecraft
        """
        
        cast.remove_actor("players", self)

        spacecraft = Spacecraft()
        x = int(constants.SCREEN_WIDTH / 2)
        y = int((constants.SCREEN_HEIGHT / 2) + (constants.SCREEN_HEIGHT / 3)) 
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        spacecraft.set_position(position)
        spacecraft.set_text("#")
        cast.add_actor("players", spacecraft)