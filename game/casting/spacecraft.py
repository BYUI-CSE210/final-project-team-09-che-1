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
        self._color = constants.BLUE
    
    def get_player(self):
        """gets the player's position"""
        
        return self.get_position()
    
    def reset(self): 
        """resets the player's into the middle of the screen
        
        args (self) = an instance of a spacecraft
        """
        
        text = self.get_text()
        
        #blink 2 times the spacecraft
        for i in range(2):    
            self.set_text("")
            self.set_text(text)
            self.set_text("")
        
        #set the position to the middle of the screen
        self.set_position(Point(int(constants.SCREEN_WIDTH / 2),int(constants.SCREEN_HEIGHT * 0.85)))
        self.set_text(text)