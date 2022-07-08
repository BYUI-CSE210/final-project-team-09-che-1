import constants
import random
from game.casting.enemy import Enemy
from game.casting.space import Space
from game.scripting.control_enemies_action import ControlEnemiesAction
from game.scripting.control_spacecraft_action import ControlSpacecraftAction
from game.scripting.control_laser_action import ControlLaserAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.directing.director import Director
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.draw_hud_action import DrawHUDAction
from game.scripting.script import Script
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_colission_action import HandleCollisionsAction
from game.shared.point import Point
from game.shared.color import Color
from game.casting.lives import Lives
from game.casting.cast import Cast
from game.casting.spacecraft import Spacecraft

def main():

    #Cast
    cast = Cast()

    #create the space craft
    spacecraft = Spacecraft()
    x = int(constants.SCREEN_WIDTH / 2)
    y = int((constants.SCREEN_HEIGHT / 2) + (constants.SCREEN_HEIGHT / 3))  
    sc_position = Point(x, y).scale(constants.CELL_SIZE)
    spacecraft.set_position(sc_position)
    spacecraft.set_text("#")

    cast.add_actor("players", spacecraft)

    #Create the BACKGROUND
    for n in range(constants.DEFAULT_BACKGROUND_OBJECTS):
        
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, 50)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        background = Space()
        background.set_position(position)
        background.set_velocity(constants.BACKGROUND_VELOCITY)
        background.set_color(constants.WHITE_B)
        background.set_font_size(constants.CELL_SIZE)

        cast.add_actor("background", background)
     
    #Create the enemies
    for n in range(constants.DEFAULT_ENEMIES):    

        text = random.choice(constants.ENEMIES)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, 12)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        enemy = Enemy()
        enemy.set_position(position)
        enemy.set_velocity(constants.ENEMIES_VELOCITY)
        enemy.set_text(text)
        enemy.set_color(constants.RED)
        enemy.set_font_size(constants.CELL_SIZE )

        cast.add_actor("enemies", enemy)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    #create the script
    script = Script()
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("input", ControlSpacecraftAction(keyboard_service))
    script.add_action("input", ControlLaserAction(keyboard_service))

    #script.add_action("input", ControlEnemiesAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    # script.add_action("update", HandleCollisionsAction())
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()

##SPACE INVADERS

## CAST:
# clase el enemigo (aliens) enemigos se mueven hacia abajo y disparan lasers //PABLO
# clase para laser (dependiendo si el enemigo /color diferente // jugador = rojo) //PABLO
# # /// velocidad del laser del jugador hacia arriba / enemigo hacia abajo
# clase para el score (si enemigo muere = 100 puntos / enemigo especial = 200 puntos) //PABLO
#       - debe llamarse en handlecollisions (metodo de colision de laser con enemigo)
# diseño del nivel 1 - jugador centro de la pantalla abajo en eje x - enemigos (varios en las primeras filas) / RENZO 

## SCRIPTING:
# clase y diseño de clase de colisiones de laser y enemigos / crear un game over collision //VALE

##SERVICES:
# investigar clase sonido y reusar lo que se pueda
# clase para sonido (explosion, enemigos, lasers)


## Extras (si hay tiempo)
# # background class = (gems and rocks moving in the screen / have no effect over the player / just background) 
# niveles (mas de uno)
# corazon aparece random en la pantalla y si laser golpea gana una vida
# 2 jugadores
