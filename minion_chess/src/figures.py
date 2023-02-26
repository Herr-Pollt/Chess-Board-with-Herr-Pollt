from enum import Enum
import pygame as pg
from utilities import load_image
class Pieces(Enum):
    PAWN = 1
    BISHOP = 2
    KNIGHT = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Piece(pg.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image, self.rect = load_image(image_path)
        self.rect.x = x
        self.rect.y = y
        
    def move():
        pass

    def capture():
        pass

class Pawn(Piece):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)

class Knight(Piece):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        
class Bishop(Piece):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)

class Rook(Piece):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)

class Queen(Piece):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)

class King(Piece):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)