import pygame as pg
from figures import Pawn
from tile import Tile

class Board(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.width, self.height = 500, 500
        self.make_tiles()
    def setup_pieces(self):
        pass
    def make_tiles(self):
        WHITE = (255, 255, 255)
        GREEN = (0, 128, 0)
        position = 1
        tilex = 0
        for i in range(8):
            tilex += float(500/8)
            tiley = 0
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = WHITE
                else:
                    color = GREEN
                tile = Tile(color, (tilex, tiley, self.width/8, self.width/8), position)
                self.add(tile)
                position += 1
                tiley += float(self.width/8)