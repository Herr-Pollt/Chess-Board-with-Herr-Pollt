import pygame as pg

class Tile(pg.sprite.Sprite):

    def __init__(self, color, position, tilex = -(float(500/8)), tiley = 0, width = float(500/8), height = float(500/8)):
        super().__init__()
        self.tile_size = (width, height)
        self.tilex = tilex
        self.tiley = tiley
        self.rect = (self.tilex, self.tiley, width, height)
        self.image = pg.Surface((width, height))
        self.visible = False

    def show(self, visible):
        self.visible = visible
