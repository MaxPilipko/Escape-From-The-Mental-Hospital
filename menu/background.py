from paths import background_path
from screen import width, height
import pygame as pg


bg = pg.image.load(background_path)
bg = pg.transform.scale(bg, (width, height))