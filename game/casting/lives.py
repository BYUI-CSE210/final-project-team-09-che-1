from constants import *
from game.casting.actor import Actor

class Lives(Actor):
    """A life is what allows the player to continue playing the game 
    
    Responsability: to keep track of the player in-game lives
    
    attributes: 
        _lives (int) = the player's amount of lives
    """

    def __init__(self):
        """creates a new instace of the lives"""

        super().__init__()
        self._lives = DEFAULT_LIVES
    
    def get_lives(self):
        """gets the amount of lives from the player"""

        return self._lives
    
    def lose_life(self):
        """removes one life from the player"""

        if self._lives > 0:
            self._lives -= 1
    
    def reset_lives(self):
        """resets the lives to the default value"""

        self._lives = DEFAULT_LIVES