import pygame as pg
from tile import Tile


tile = Tile()

class Screen():
    screen_width, screen_height = 500, 500
    screen = pg.display.set_mode((screen_width, screen_height))
    
    def __init__(self):
        pass
    
    def MakeScreen(self):
        pg.display.update()
        self.screen.blit(self.screen, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_loop = False
                pg.quit()
        tile.make_tiles(self.screen)