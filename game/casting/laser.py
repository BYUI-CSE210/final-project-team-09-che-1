import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast

class Laser(Actor):
    """An artifact in this game could be a rock or a gem
    
    The responsability of the artifact is to keep track of the 
    score earned by the player
    
    Attributes:
        score (int) = the score earned depending if the character is a gem or a rock
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

    
    
   