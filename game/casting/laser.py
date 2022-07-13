import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point

class Laser(Actor):
	"""A laser is something that the player shoots using the 
	space bar key
	
	The responsabilit of the laser is to use colission to defeat enemies
	or destroy the player
	
	Attributes:
		_color (color): color to identidy the laser (green) 
		_text (string): a string to identify the laser |
	"""

	def __init__(self):
		"""constructs a new instance of a laser"""

		super().__init__()
		self._color = constants.GREEN
		self._text = "|"
	
	def spawn(self, cast):
		"""spawns the laser in front of the player
		
		args: 
			cast: the cast of the game containing the actors
		"""

		spacecraft = cast.get_first_actor("players")
		player_pos = spacecraft.get_position()
		
		position = player_pos.add(Point(0, 1 * constants.CELL_SIZE))
		self.set_position(position)
	
	def enemy_laser(self, enemy):
		"""spawns enemy laser
		
		args: 
			enemy: the enemy that will fire the laser
		"""

		enemy_pos = enemy.get_position()
		position = enemy_pos.add(Point(0, 1 * constants.CELL_SIZE))
		self.set_position(position)
		

	def move_next(self):
		"""makes the laser vanish istead of wrapping it"""

		x = (self._position.get_x() + self._velocity.get_x())
		y = (self._position.get_y() + self._velocity.get_y()) 
		self._position = Point(x, y)

	def reset(self, cast, type):
		"""removes the laser from the game to give the 
		player some time to recover
		
		args: 
			cast: the cast of the game
		"""

		if type == "enemy":
			cast.remove_actor("enemy_laser", self)
		elif type == "player":
			cast.remove_actor("lasers", self)
