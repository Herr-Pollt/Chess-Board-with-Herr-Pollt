import pygame as pg

class Tile():
    WHITE = (255, 255, 255)
    GREEN = (0, 128, 0)

    def __init__(self, tilex = -(float(500/8)), tiley = 0, width = float(500/8), height = float(500/8)):
        self.tile_size = (width, height)
        self.tilex = tilex
        self.tiley = tiley
    def make_tiles(self, screen):
        for i in range(8):
            self.tilex += float(500/8)
            self.tiley = 0
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = self.WHITE
                else:
                    color = self.GREEN
                pg.draw.rect(screen, color, (self.tilex, self.tiley, self.tile_size[0], self.tile_size[1]))
                self.tiley += float(500/8)