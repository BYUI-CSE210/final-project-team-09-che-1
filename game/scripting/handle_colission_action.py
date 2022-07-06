import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a player collides
    with the other player's trail, and vice versa, or the game is over.

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
       
            self.handle_player_collition(cast)
            self._handle_game_over(cast)


    def handle_player_collition(self, cast):
        """Sets the game over flag if the player collides with the trail of the other player 
        or with the head of the other player
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        #get player
        shots = cast.get_actors("shots")
        shot = shots[0]
        player = cast.get_actors("player")
        player1 = shots[0]
        enemies = cast.get_actors("enemies")
        #red_enemies = enemies[0]
        #blue_enemies = enemies [1]

        #get the scores
        scores = cast.get_actors("scores")
        score_p1 = scores[0]
    

        #if the shot collides with enemies
        for enemy in enemies:
            if shot.get_position().equals(enemy.get_position()):
                if enemy.get_text() == "*":
                #add points to the player
                    score_p1.add_points(100)
                if enemy.get_text() == "O":
                    score_p1.add_points(200)
              

        #if the player collides with enemies
        for enemy in enemies:
            if player.get_position().equals(enemies.get_position()):
                self._is_game_over = True
                #add points to the other player 
   

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the players and trails white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        if self._is_game_over:
            #get the player
            player = cast.get_actors("players")
            player1 = player[0]
            

            #get the lives
            lives = cast.get_actors("lives")
            live    = lives[0].get_lives()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            if live > 0:
                message = Actor()
                message.set_text("Try Again")
                message.set_position(position)
                message.set_color(constants.BLUE)
                cast.add_actor("messages", message)
   
            else: 
                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                message.set_color(constants.BLUE)
                cast.add_actor("messages", message)

