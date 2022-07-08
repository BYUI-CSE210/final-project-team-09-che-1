import pyray
import constants
from game.casting.spacecraft import Spacecraft
from game.scripting.action import Action
from game.shared.point import Point
#from game.scripting.handle_colission_action import HandleCollisionsAction

class ControlSpacecraftAction(Action):
    """
    An input action that controls the spacecraft's movement.
    
    The responsibility of ControlActorsAction is to get the direction and move the spacecraft.
<<<<<<< HEAD
=======

>>>>>>> 011a7bc8a646e9d69b268d804259611f0ce67154
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _direction (Point): a point to direct the spacecraft
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

        dx = 0
        dy = 0

        if self._keyboard_service.is_key_down("a"):
            dx = -1
        
        if self._keyboard_service.is_key_down("d"):
            dx = 1
        
        self._direction = Point(dx, dy)
        self._direction = self._direction.scale(constants.CELL_SIZE)
        spacecraft = cast.get_first_actor("players")
        spacecraft.set_velocity(self._direction) 