import pygame as pg

class Screen():
    screen_width, screen_height = 500, 500
    screen = pg.display.set_mode((screen_width, screen_height))
    
    def __init__(self):
        pass
    
    def MakeScreen(self):
        pg.display.update()
        self.screen.blit(self.screen, (0, 0))