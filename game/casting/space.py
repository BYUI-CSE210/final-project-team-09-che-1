import constants
import random
from game.casting.actor import Actor

class Space(Actor):
    """The background of the game formed by stars and rocks in the space

    The responsability of the space is to add style to the background of the 
    screen while it is open
    
    Attributes:
        _text (string) = the text representation of the rocks or star in the space
    """
    
    def __init__(self):
        """construct a new instance of the space"""   

        super().__init__()
        self._text = random.choice(constants.BACKGROUND)
    
