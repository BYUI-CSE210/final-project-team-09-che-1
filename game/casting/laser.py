import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Laser(Actor):
	"""A laser is something that the player shoots using the 
	space bar key
	
	The responsabilit of the laser is to use colission to defeat enemies
	or destroy the player
	
	Attributes:
		_color (color): color to identidy the laser (green) 
	"""

	def __init__(self):
		"""constructs a new instance of a laser"""

		super().__init__()
		self._color = constants.GREEN
	
	def spawn(self, cast):
		"""spawns the laser in front of the player"""

		spacecraft = cast.get_first_actor("players")
		player_pos = spacecraft.get_position()
		
		position = player_pos.add(Point(0, 1 * constants.CELL_SIZE))
		self.set_position(position)
		self.set_text("|")
	
	def move_next(self):
		"""makes the laser vanish istead of wrapping it"""

		x = (self._position.get_x() + self._velocity.get_x())
		y = (self._position.get_y() + self._velocity.get_y()) 
		self._position = Point(x, y)
