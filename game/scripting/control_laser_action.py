import constants
from game.casting.laser import Laser
from game.scripting.action import Action
from game.shared.point import Point

class ControlLaserAction(Action):
    """
    An input action that controls the spacecraft's movement.
    
    The responsibility of ControlActorsAction is to get the direction and move the spacecraft.
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

        if self._keyboard_service.is_key_down("space"):

            laser = Laser()
            laser.spawn(cast)        
            laser.set_velocity(constants.LASER_VELOCITY)

            cast.add_actor("lasers", laser)
    