import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast
#from scripting.move_actors_action import MoveActorsAction

class Spacecraft(Actor):
    """An artifact in this game could be a rock or a gem
    
    The responsability of the artifact is to keep track of the 
    score earned by the player
    
    Attributes:
        score (int) = the score earned depending if the character is a gem or a rock
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        super().__init__()
        self._spacecraft = "#" 
        self._position = ""
        self._spacecraftcolor = constants.WHITE
    
    def get_player(self):

        #Creating the spacecraft
        player = Actor()
        player.set_color(constants.WHITE)
        player.set_position(constants.position)
        player.set_font_size(constants.FONT_SIZE)
        player.set_text(self._spacecraft)
        cast = Cast()
        cast.add_actor("players", player)
    
    def prepare_player(self):
        """Prepare the player to be drawn"""
        
        x = int(constants.SCREEN_HEIGHT )
        y = int(constants.SCREEN_WIDTH )

        position = Point(x,y)
        velocity = Point(constants.CELL_SIZE, 0)

        spacecraft = Actor()
        spacecraft.set_position(position)
        spacecraft.set_velocity(velocity)
        spacecraft.set_text(self._spacecraft)
        spacecraft.set_color(self._spacecraftcolor)


    def move_next(self):
        """Moves the player"""
        return self._spacecraft.move_next()