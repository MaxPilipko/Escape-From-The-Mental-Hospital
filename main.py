import pygame as pg
pg.init()

from window import screen
from button import buttons, funcs_button


def run_game():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.win.fill((0, 0, 0))
        funcs_button.update(screen=screen.win, funcs_dict=funcs_button.funcs_dict)
        pg.display.flip()


run_game()