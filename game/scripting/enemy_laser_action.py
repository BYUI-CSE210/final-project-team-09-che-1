import random
import constants
from game.scripting.action import Action
from game.casting.laser import Laser

class EnemyLaserAction(Action):
    """
    An update action that spawns an enemy laser.
    
    The responsibility of EnemyLaserAction is to spawn an enemy laser after certain time.

    Attributes:
        _counter (int) : a counter to keep track of the seconds passed in the game
    """

    def __init__(self):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            self: An instance of enemylaseraction.
        """
        
        self._counter = 0

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        self._counter += 1
        if self._counter >= (constants.FRAME_RATE * 2):
            #reset the counter
            self._counter = 0

            enemies = cast.get_actors("enemies")
            e_lasers = 9

            if len(enemies) >= e_lasers:
                firing_enemies = random.sample(enemies, e_lasers)
                for enemy in firing_enemies:    
                    laser = Laser()
                    laser.enemy_laser(enemy)
                    laser.set_velocity(constants.ENEMY_LASER_VELOCITY)
                    laser.set_color(constants.YELLOW)

                    cast.add_actor("enemy_laser", laser)
            else:
                e_lasers = len(enemies)
                firing_enemies = random.sample(enemies, e_lasers)
                for enemy in firing_enemies:
                    laser = Laser()
                    laser.enemy_laser(enemy)
                    laser.set_velocity(constants.ENEMY_LASER_VELOCITY)
                    laser.set_color(constants.YELLOW)

                    cast.add_actor("enemy_laser", laser)


