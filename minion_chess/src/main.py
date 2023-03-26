from screen import Screen
import pygame as pg
from tile import Tile
from side import Side
from config import Config
from board import Board

def main():
    game_loop = True
    config = Config()
    screen = Screen()
    p1 = Side(0, 0)
    p2 = Side(config.screen_height/8*7, config.screen_height/8*5)
    pg.init()
    board = Board()
    while game_loop:
        #TODO: do not make the screen everytime, rather create a container similar to p1 
        # that will draw the objects inside. Then later, we can access the tiles in that
        # container more easily.
        # make a design plan with figma
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_loop = False
                pg.quit()
        screen.MakeScreen()
        p1.draw(screen.screen)
        p2.draw(screen.screen)
        board.draw(screen.screen)
if __name__ == "__main__":
    main()