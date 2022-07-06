import constants
from game.shared.point import Point
from game.shared.color import Color
from game.casting.lives import Lives

##SPACE INVADERS

# agregar el readme y crear las reglas del juego /VALE
# crear un archivo de constantes /RENZO

## CAST:
# Class cast, actor
# clase el jugador (navecita) //PABLO
# clase el enemigo (aliens) enemigos se mueven hacia abajo y disparan lasers //PABLO
# clase para laser (dependiendo si el enemigo /color diferente // jugador = rojo) //PABLO
# # /// velocidad del laser del jugador hacia arriba / enemigo hacia abajo
# clase para el score (si enemigo muere = 100 puntos / enemigo especial = 200 puntos) //PABLO
#       - debe llamarse en handlecollisions (metodo de colision de laser con enemigo)
# diseño del nivel 1 - jugador centro de la pantalla abajo en eje x - enemigos (varios en las primeras filas) / RENZO 
# clase para las vidas (vanish y re-draw in the center) /RENZO

## SCRIPTING:
#script class //REUSAR
# action class (interface / execute method to be overriden) //REUSAR
# clase y diseño de clase de colisiones de laser y enemigos / crear un game over collision //VALE
# crear una interfaz - optional - ?
# clase solo para dibujar los personajes / clase solo para dibujar el HUD (draw_hud_action) (draw_actors_action) //RENZO
# clase para el director (ejecutar las acciones) //REUSAR - AJUSTAR 
# clase para el movimiento del jugador(es - moveactors) //REUSAR

## SHARED:
# Class Color y Point //REUSAR - ADD COLORS

##SERVICES:
# class Keyboard / Video //REUSAR
# investigar clase sonido y reusar lo que se pueda
# clase para sonido (explosion, enemigos, lasers)


## Extras (si hay tiempo)
# # background class = (gems and rocks moving in the screen / have no effect over the player / just background) 
# niveles (mas de uno)
# corazon aparece random en la pantalla y si laser golpea gana una vida
# 2 jugadores
