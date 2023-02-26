import pygame as pg
def load_image(image_path, colorkey=-1, scale=0.32):
    image = pg.image.load(image_path)
    #pg.blit()
    size = image.get_size()
    size = (int(size[0]*scale), int(size[1]*scale))
    image = pg.transform.scale(image, size)
    image = image.convert()
    rect = image.get_rect()

    if colorkey is not None:
        if colorkey==-1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, rect