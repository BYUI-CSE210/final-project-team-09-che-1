from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    The responsibility of DrawActorsAction is to draw all the actors.
    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """
    
    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        spacecraft = cast.get_first_actor("players")
        background = cast.get_actors("background")
        enemy = cast.get_actors("enemies")
        laser = cast.get_actors("lasers")
        score = cast.get_first_actor("scores")
        lives = cast.get_first_actor("lives")


        self._video_service.clear_buffer()
        self._video_service.draw_actor(spacecraft)
        self._video_service.draw_actors(background)
        self._video_service.draw_actors(enemy)
        self._video_service.draw_actors(laser)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(lives)
        self._video_service.flush_buffer()