import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['a'] = pyray.KEY_A
        self._keys['d'] = pyray.KEY_D
<<<<<<< HEAD
        self._keys['f'] = pyray.KEY_F
=======
        self._keys['space'] = pyray.KEY_SPACE
>>>>>>> 011a7bc8a646e9d69b268d804259611f0ce67154

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (a, d, space)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (a, d, space)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)