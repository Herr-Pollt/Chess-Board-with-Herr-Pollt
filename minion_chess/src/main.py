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
        screen.MakeScreen()
        p1.draw(screen.screen)
        p2.draw(screen.screen)
if __name__ == "__main__":
    main()