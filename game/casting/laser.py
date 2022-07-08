import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast

class Laser(Actor):
    """A laser is something that the player shoots with the space bar key
    
    The responsability of the laser is to use collisions to defeat enemies
    or to destroy the player
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        super().__init__()
        
    
    def get_player(self):
        """Return the Spacecraft"""
        pass
        #Creating the spacecraft
     #   player = Actor()
     #   player.set_color(constants.GREEN)
       # player.set_position(position)
      #  player.set_font_size(constants.FONT_SIZE)
      #  player.set_text("#")
        #cast = Cast()
       # cast.add_actor("player1", player)

    
    
   