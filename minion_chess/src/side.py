import pygame as pg
from figures import Pawn, Bishop, Knight, Rook, Queen, King
from config import Config

config = Config()
class Side(pg.sprite.Group):
    
    def __init__(self, threshold, threshold2):
        super().__init__()
        for i in range(8):
            x, y = config.screen_width/8*i, config.screen_height/8 + threshold2
            pawn = Pawn("minion_chess\src\images\Pawn.png", x, y)
            self.add(pawn)
        x, y = 0, 0 + threshold
        rook = Rook("minion_chess\src\images\Rook.png", x, y)
        self.add(rook)

        x, y = config.screen_width/8*7, 0 + threshold
        rook = Rook("minion_chess\src\images\Rook.png", x, y)
        self.add(rook)

        x, y = config.screen_width/8, 0 + threshold
        knight = Knight("minion_chess\src\images\Knight.png", x, y)
        self.add(knight)

        x, y = config.screen_width/8*6, 0 + threshold
        knight = Knight("minion_chess\src\images\Knight.png", x, y)
        self.add(knight)

        x, y = config.screen_width/8*2, 0 + threshold
        bishop = Bishop("minion_chess\src\images\Bishop.png", x, y)
        self.add(bishop)

        x, y = config.screen_width/8*5, 0 + threshold
        bishop = Bishop("minion_chess\src\images\Bishop.png", x, y)
        self.add(bishop)

        x, y = config.screen_width/8*4, 0 + threshold
        king = King("minion_chess\src\images\King.png", x, y)
        self.add(king)

        x, y = config.screen_width/8*3, 0 + threshold
        queen = Queen("minion_chess\src\images\Queen.png", x, y)
        self.add(queen)