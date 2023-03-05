from screen import Screen
import pygame as pg
from tile import Tile
from side import Side
from config import Config

def main():
    game_loop = True
    config = Config()
    screen = Screen()
    p1 = Side(0, 0)
    p2 = Side(config.screen_height/8*7, config.screen_height/8*5)
    pg.init()
    while game_loop:
        #TODO: do not make the screen everytime, rather create a container similar to p1 
        # that will draw the objects inside. Then later, we can access the tiles in that
        # container more easily.
        # make a design plan with figma
        screen.MakeScreen()
        p1.draw(screen.screen)
        p2.draw(screen.screen)
if __name__ == "__main__":
    main()