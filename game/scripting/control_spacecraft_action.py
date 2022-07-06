import constants
from game.scripting.action import Action
from game.shared.point import Point
#from game.scripting.handle_colission_action import HandleCollisionsAction

class ControlSpacecraftAction(Action):
    """
    An input action that controls the player 1 movements.
    
    The responsibility of ControlActorsAction is to get the direction and move the player 1.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """

        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
       # if self._keyboard_service.is_key_down('w'):
         #   self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
       # if self._keyboard_service.is_key_down('s'):
         #   self._direction = Point(0, constants.CELL_SIZE)
        
        spacecraft = cast.get_first_actor("players")
        spacecraft.move_next()
        #spacecraft.turn_player(self._direction)
        #spacecraft.grow_trail()
        
        score = cast.get_first_actor("scores")
        points = 1
        score.add_points(points)