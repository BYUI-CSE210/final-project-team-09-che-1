import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a player or laser collides
    with the enemies vice versa, or the game is over.

    Attributes:
        is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""

        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        if not self._is_game_over:
            self.handle_laser_collition(cast)
            self._handle_game_over(cast)
            


    def handle_laser_collition(self, cast):
        """Modify lives and the score if the shots collides with the enemies 
        or the enemy's lasers collides with the player.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        #get lasers - player - enemies
        lasers = cast.get_actors("lasers")
        enemy_lasers = cast.get_actors("enemy_laser")
        player = cast.get_first_actor("players")
        
        
        #get the score
        score = cast.get_first_actor("scores")

        if bool(lasers):
            for laser in lasers:
                l_position = laser.get_position()
                enemies = cast.get_actors("enemies")
                
                #if the laser collides with enemies
                for enemy in enemies:
                    e_position = enemy.get_position()
                    # if l_position.equals((enemy.get_enemy()).add(Point(constants.CELL_SIZE, constants.CELL_SIZE))):
                    if e_position.get_x() <= l_position.get_x() and l_position.get_x() <= (e_position.get_x() + constants.CELL_SIZE):
                        if e_position.get_y() <= l_position.get_y() and l_position.get_y() <= (e_position.get_y() + constants.CELL_SIZE):
                            #add points to the player
                            score.add_points(100)
                            enemy.vanish(cast)
                            laser.reset(cast, "player")

        if bool(enemy_lasers):
            for laser in enemy_lasers:        
                el_position = laser.get_position()
                p_position = player.get_position()

                #if enemy laser collides with player
                if p_position.get_x() <= el_position.get_x() and el_position.get_x() <= (p_position.get_x() + constants.CELL_SIZE):
                    if p_position.get_y() <= el_position.get_y() and el_position.get_y() <= (p_position.get_y() + constants.CELL_SIZE):
                        #lose one life
                        lives = cast.get_first_actor("lives")
                        lives.lose_life()
                        player.reset(cast)
                        for laser in enemy_lasers:
                            laser.reset(cast, "enemy")


    def _handle_game_over(self, cast):
        """Shows the 'game over' message if the game is over or the player lose all lives. 
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        #get the lives
        lives = cast.get_first_actor("lives")
        live = lives.get_lives()
        #enemies
        enemies = cast.get_actors("enemies")

        if live == 0:
            self._is_game_over = True

            x = int(constants.SCREEN_WIDTH / 2)
            y = int(constants.SCREEN_HEIGHT / 2)
            position = Point(x, y)
            
            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            message.set_color(constants.BLUE)
            cast.add_actor("messages", message) 

        if not bool(enemies):
            self._is_game_over = True

            x = int(constants.SCREEN_WIDTH / 2)
            y = int(constants.SCREEN_HEIGHT / 2)
            position = Point(x, y)
            
            message = Actor()
            message.set_text("Congrats, You Win!")
            message.set_position(position)
            message.set_color(constants.BLUE)
            cast.add_actor("messages", message) 